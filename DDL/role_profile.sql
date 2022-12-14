CREATE EXTERNAL TABLE aspen_db.role_profile(
  role_profile_id bigint,
  user_id bigint,
  role_profile_type_id bigint,
  created bigint,
  created_by string,
  updated bigint,
  updated_by string
)
STORED AS PARQUET
LOCATION 's3://aspen-code-challenge/data/user/'
tblproperties ("parquet.compression"="SNAPPY");