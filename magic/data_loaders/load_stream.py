from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from os import path, getenv
import duckdb
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_s3_bucket(*args, **kwargs):

    key_id = getenv('AWS_ACCESS_KEY_ID')
    key_value = getenv('AWS_SECRET_ACCESS_KEY')
    
    conn = duckdb.connect()
    conn.execute("INSTALL httpfs;")
    conn.execute("LOAD httpfs;")


    conn.execute(f"SET s3_region='us-east-2';")
    conn.execute(f"SET s3_access_key_id='{key_id}';")
    conn.execute(f"SET s3_secret_access_key='{key_value}';")

    bucket_name = 'ahhh-buck-it'
    object_path = 'taxi_data_stream'

    path = 's3://ahhh-buck-it/taxi_data_stream/*.parquet'
    db = conn.sql(f"SELECT * FROM read_parquet('{path}');")

    return db.df()

@test
def test_columns(output, *args) -> None:
    """
    Test the number of columns.
    """
    assert (len(output.columns) == 9)

@test
def test_status(output, *args) -> None:
    """
    Test the status column to ensure expected values
    """

    def check_equal(L1, L2):
        return len(L1) == len(L2) and sorted(L1) == sorted(L2)

    expected_status = ['enroute', 'dropoff', 'pickup']

    assert check_equal(output.ride_status.unique(), expected_status)