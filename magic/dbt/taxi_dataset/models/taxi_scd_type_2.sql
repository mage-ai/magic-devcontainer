{{
  config(
    materialized = "table"
  )
}}

WITH base AS (
  SELECT
    ride_id,
    _timestamp::timestamptz as timestamp,
    ride_status
  FROM
    {{ ref('taxi_stream_raw') }}
),
did_cg AS (
  SELECT
    *,
    (
      (
        LAG(ride_status) OVER (
          PARTITION BY ride_id
          ORDER BY
            timestamp
        ) <> ride_status
      )
      OR (
        LAG(ride_status) OVER (
          PARTITION BY ride_id
          ORDER BY
            timestamp
        ) IS NULL
      )
    ) as did_change
  FROM
    base
)
SELECT
  ride_id,
  ride_status,
  timestamp as start_ts,
  COALESCE(LEAD(timestamp) OVER (
    PARTITION by ride_id
    ORDER BY
      timestamp
  ), timestamp) as end_ts,
  LEAD(timestamp) OVER (
    PARTITION by ride_id
    ORDER BY
      timestamp
  ) IS NULL as is_current_row
FROM
  did_cg
WHERE
  did_change