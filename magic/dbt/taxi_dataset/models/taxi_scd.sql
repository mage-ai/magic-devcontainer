{{
  config(
    materialized = "table",
  )
}}

SELECT * FROM {{ source('mage_taxi_dataset','dbt_demo_load_stream') }}