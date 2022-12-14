import boto3

#libs that will need to be added
import pandas as pd
import io
import time
import pyarrow as pa
import pyarrow.parquet as pq
# add openpyxl

AccessKeyID = 'AKIA5BNPANSXWRDRJLS7'
SecretAccessKey = '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'

BUCKET = 'aspen-code-challenge'
SOURCE_DATA_PATH = 'data/source-excel/data_engineer_raw_data.xlsx'


class Boto4:
    def __init__(self):
        self.s3 = boto3.client('s3', aws_access_key_id=AccessKeyID, aws_secret_access_key=SecretAccessKey)

    def get_data(self, bucket, key):
        obj = self.s3.get_object(Bucket=bucket, Key=key)
        df = pd.ExcelFile(io.BytesIO(obj['Body'].read()))
        return df

    def save_parquet_to_s3(self, df, bucket, key, filename):
        df.to_parquet(io.BytesIO(), index=False)
        self.s3.put_object(Body=io.BytesIO().getvalue(), Bucket=bucket, Key=key)


if __name__ == '__main__':

    # Get main data source - currently on s3
    a = Boto4()
    df = a.get_data(bucket=BUCKET, key=SOURCE_DATA_PATH)
    df_borrower = pd.read_excel(df, 'borrower')
    df_role_profile = pd.read_excel(df, 'role_profile')

    # email type
    file_path = 'data/email_type/'
    filename = 'email_type.parquet'


    # email

    # address

    # phone number type

    # phone number

    # role profile

    # user

    # role profile type

    # user profile
