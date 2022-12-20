import boto3
import io
import pandas as pd


AccessKeyID = ''
SecretAccessKey = ''


class Boto4:
    def __init__(self, bucket='aspen-code-challenge'):
        self.s3 = boto3.client('s3', aws_access_key_id=AccessKeyID, aws_secret_access_key=SecretAccessKey)
        self.bucket = bucket

    def get_data(self, key):
        obj = self.s3.get_object(Bucket=self.bucket, Key=key)
        df = pd.ExcelFile(io.BytesIO(obj['Body'].read()))
        return df

    def save_parquet_to_s3(self, df, key, filename):
        buffer = io.BytesIO()
        df.to_parquet(buffer, index=False)
        key_file = key + '/' + filename
        self.s3.put_object(Body=buffer.getvalue(), Bucket=self.bucket, Key=key_file)