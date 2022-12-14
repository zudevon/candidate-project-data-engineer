CREATE EXTERNAL TABLE aspen_db.user_profile(
  user_profile_id bigint,
  first_name string,
  last_name string,
  created_date bigint,
  created_by string,
  updated bigint,
  updated_by string
)
STORED AS PARQUET
LOCATION 's3://aspen-code-challenge/data/user_profile/'
tblproperties ("parquet.compression"="SNAPPY");