CREATE EXTERNAL TABLE aspen_db.users(
  user_id bigint,
  user_profile_id bigint,
  created bigint,
  created_by string,
  updated bigint,
  updated_by string
)
STORED AS PARQUET
LOCATION 's3://aspen-code-challenge/data/user/'
tblproperties ("parquet.compression"="SNAPPY");