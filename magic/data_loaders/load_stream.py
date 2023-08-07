import os
import awswrangler as wr

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_s3_bucket(*args, **kwargs):

    df = wr.s3.read_parquet(path="s3://ahhh-buck-it/taxi_data_stream/", dataset=True)

    return df

@test
def test_columns(output, *args) -> None:
    """
    Test the number of columns.
    """

    expected_cols = ['ride_id', 
                     'point_idx', 
                     'latitude', 
                     'longitude', 
                     'timestamp', 
                     'meter_reading', 
                     'meter_increment', 
                     'ride_status', 
                     'passenger_count'
                     ]
    assert set(expected_cols).issubset(set(output.columns))

@test
def test_status(output, *args) -> None:
    """
    Test the status column to ensure expected values
    """

    def check_equal(L1, L2):
        return len(L1) == len(L2) and sorted(L1) == sorted(L2)

    expected_status = ['enroute', 'dropoff', 'pickup']

    assert check_equal(output.ride_status.unique(), expected_status)
