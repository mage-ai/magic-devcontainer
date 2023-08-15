import psycopg2
import pandas as pd
from os import path, getenv

conn = psycopg2.connect(
        host=getenv('POSTGRES_HOST'),
        port=getenv('PG_HOST_PORT'),
        database=getenv('POSTGRES_DB'),
        user=getenv('POSTGRES_USER'),
        password=getenv('POSTGRES_PASSWORD')
    )


with conn:
    sql = """
        WITH sample_user AS (
            SELECT
                ride_id,
                COUNT(DISTINCT ride_status) as status_count
            FROM postgres.taxi_stream_raw
            GROUP BY 1
            HAVING COUNT(DISTINCT ride_status) = 3
            ORDER BY RANDOM()
            LIMIT 1
        )
            SELECT
                ride_id,
                ride_status,
                start_ts,
                end_ts,
                EXTRACT(EPOCH FROM end_ts - start_ts) as duration_seconds,
                is_current_row
            FROM postgres.taxi_scd_type_2
            INNER JOIN sample_user
                USING(ride_id)
            ORDER BY start_ts DESC;
            """

    display(pd.read_sql_query(sql, conn))