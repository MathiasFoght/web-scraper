from datetime import datetime, timezone
from psycopg.types.json import Json
from ..db import Database

class ProductRepository:
    def __init__(self, db: Database):
        self.db = db

# Initialize the database schema (only if needed)
    def _init_schema(self):
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    id BIGSERIAL PRIMARY KEY,
                    asin TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                    data JSONB NOT NULL
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS product_snapshots (
                    id BIGSERIAL PRIMARY KEY,
                    asin TEXT NOT NULL,
                    scraped_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                    data JSONB NOT NULL
                );
            """)
            cur.execute("""
                CREATE INDEX IF NOT EXISTS product_snapshots_asin_scraped_at_idx
                ON product_snapshots (asin, scraped_at DESC);
            """)
            conn.commit()

    def insert_product(self, product_data):
        print('Inserting product')
        asin = product_data.get("asin")
        if not asin:
            raise ValueError("product_data must include 'asin'")

        created_at = product_data.get("created_at")
        if not created_at:
            created_at = datetime.now(timezone.utc)
            product_data["created_at"] = created_at.isoformat()

        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute("""
                INSERT INTO products (asin, created_at, data)
                VALUES (%s, %s, %s)
                ON CONFLICT (asin)
                DO UPDATE SET
                    created_at = EXCLUDED.created_at,
                    data = EXCLUDED.data;
            """, (asin, created_at, Json(product_data)))
            cur.execute("""
                INSERT INTO product_snapshots (asin, scraped_at, data)
                VALUES (%s, %s, %s);
            """, (asin, created_at, Json(product_data)))

            conn.commit()

        return asin

    def get_product(self, asin):
        print('Fetching product')
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(
                "SELECT data FROM products WHERE asin = %s LIMIT 1;",
                (asin,)
            )
            row = cur.fetchone()

        return row["data"] if row else None

    def get_all_products(self):
        print('Fetching all products')
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT data
                FROM products
                ORDER BY created_at DESC;
            """)
            rows = cur.fetchall()

        return [row["data"] for row in rows]

    def search_products(self, search_criteria):
        print('Searching products')
        if not search_criteria:
            return []

        where_parts = []
        params = []

        for key, value in search_criteria.items():
            where_parts.append("data ->> %s = %s")
            params.extend([key, str(value)])

        sql = (
            "SELECT data FROM products "
            "WHERE " + " AND ".join(where_parts) + " "
            "ORDER BY created_at DESC;"
        )

        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()

        return [row["data"] for row in rows]

    def get_latest_snapshot(self, asin):
        print('Fetching latest snapshot')
        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT data
                FROM product_snapshots
                WHERE asin = %s
                ORDER BY scraped_at DESC
                LIMIT 1;
            """, (asin,))
            row = cur.fetchone()

        return row["data"] if row else None

    def get_product_snapshots(self, asin, limit=50, offset=0):
        print('Fetching product snapshots')
        if limit < 0:
            raise ValueError("limit must be non-negative")
        if offset < 0:
            raise ValueError("offset must be non-negative")

        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT data
                FROM product_snapshots
                WHERE asin = %s
                ORDER BY scraped_at DESC
                LIMIT %s OFFSET %s;
            """, (asin, limit, offset))
            rows = cur.fetchall()

        return [row["data"] for row in rows]

    def get_price_history(self, asin, days=30, limit=300):
        print('Fetching price history')
        if days <= 0:
            raise ValueError("days must be greater than 0")
        if limit <= 0:
            raise ValueError("limit must be greater than 0")

        with self.db.connection() as conn, conn.cursor() as cur:
            cur.execute("""
                SELECT scraped_at, data
                FROM (
                    SELECT scraped_at, data
                    FROM product_snapshots
                    WHERE asin = %s
                      AND scraped_at >= NOW() - (%s * INTERVAL '1 day')
                    ORDER BY scraped_at DESC
                    LIMIT %s
                ) snapshots
                ORDER BY scraped_at ASC;
            """, (asin, days, limit))
            rows = cur.fetchall()

        history = []
        for row in rows:
            payload = row["data"] or {}
            history.append({
                "scraped_at": row["scraped_at"],
                "price": payload.get("price"),
                "currency": payload.get("currency"),
            })
        return history
