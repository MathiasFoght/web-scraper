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