import psycopg2
conn = psycopg2.connect(
        host="host.docker.internal",
        port="5432",
        database="postgres",
        user="postgres",
        password="postgres"
    )

with conn:
    sql = """
            select ride_status, start_ts, end_ts, is_current_row from postgres.taxi_scd_type_2 
            WHERE ride_id = '778472f9-c314-4b05-b5e5-73dc585e585b'
            ORDER BY start_ts DESC;
            """
    dat = pd.read_sql_query(sql, conn)

    display(dat)