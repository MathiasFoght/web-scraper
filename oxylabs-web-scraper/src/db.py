import os
from datetime import datetime, timezone
from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Json

load_dotenv()


class Database:
    def __init__(self, db_path="data.json"):
        # Keep db_path argument for backward compatibility with previous TinyDB API.
        self.db_path = db_path
        self.host = os.getenv("POSTGRES_HOST")
        self.port = int(os.getenv("POSTGRES_PORT"))
        self.name = os.getenv("POSTGRES_DB")
        self.user = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        self._init_schema()

    #---------------------------------------------------------------------------------------
    # Configure connection

    # Func. to build connection string
    def _dsn(self):
        return (
            f"host={self.host} port={self.port} dbname={self.name} "
            f"user={self.user} password={self.password}"
        )

    # Func. to create connection to database
    def _connection(self):
        return psycopg.connect(self._dsn(), row_factory=dict_row)

    #---------------------------------------------------------------------------------------

    # Func. to create table if not exists
    def _init_schema(self):
        with self._connection() as conn, conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS products (
                    id BIGSERIAL PRIMARY KEY,
                    asin TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
                    data JSONB NOT NULL
                );
                """
            )
            conn.commit()

    # Func. insert product
    def insert_product(self, product_data):
        asin = product_data.get("asin")
        if not asin:
            raise ValueError("product_data must include 'asin'")

        created_at = product_data.get("created_at")
        if not created_at:
            created_at = datetime.now(timezone.utc).isoformat()
            product_data["created_at"] = created_at

        with self._connection() as conn, conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO products (asin, created_at, data)
                VALUES (%s, %s::timestamptz, %s::jsonb)
                ON CONFLICT (asin)
                DO UPDATE SET
                    created_at = EXCLUDED.created_at,
                    data = EXCLUDED.data;
                """,
                (asin, created_at, Json(product_data)),
            )
            conn.commit()
        return asin

    # Func. to get product by asin
    def get_product(self, asin):
        with self._connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT data FROM products WHERE asin = %s LIMIT 1;", (asin,))
            row = cur.fetchone()
        return row["data"] if row else None

    # Func. to get all products
    def get_all_products(self):
        with self._connection() as conn, conn.cursor() as cur:
            cur.execute(
                """
                SELECT data
                FROM products
                ORDER BY created_at DESC;
                """
            )
            rows = cur.fetchall()
        return [row["data"] for row in rows]

    # Func. to search products
    def search_products(self, search_criteria):
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

        with self._connection() as conn, conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()
        return [row["data"] for row in rows]
