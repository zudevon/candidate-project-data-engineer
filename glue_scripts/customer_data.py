#libs that will need to be added
import pandas as pd
import time

# boto4
from boto4 import Boto4

AccessKeyID = 'AKIA5BNPANSXWRDRJLS7'
SecretAccessKey = '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'

SOURCE_DATA_PATH = 'data/source-excel/data_engineer_raw_data.xlsx'


def main():
    # Get main data source - currently on s3
    a = Boto4()
    df = a.get_data(key=SOURCE_DATA_PATH)
    df_borrower = pd.read_excel(df, 'borrower')
    df_role_profile = pd.read_excel(df, 'role_profile').rename(columns={"borrower_id": "id"})

    # Join dataframes to have id associated with role_profiles
    df_full = df_borrower.merge(df_role_profile, on="id")
    # Give user profile ID an association to UUID/id
    df_full['user_profile_id'] = range(1000, len(df_full) + 1000)

    # TABLES

    created_date = int(time.time())
    list_of_dfs = []

    # user_profile
    df_user_profile = df_full[['user_profile_id', 'full_name']]
    df_user_profile['first_name'] = df_user_profile['full_name'].map(lambda name: name.split(" ")[0])
    df_user_profile['last_name'] = df_user_profile['full_name'].map(lambda name: name.split(" ")[1])
    df_user_profile = df_user_profile[['user_profile_id', 'first_name', 'last_name']]
    list_of_dfs.append({'name': 'user_profile', 'dataframe': df_user_profile})

    # user
    df_user = df_user_profile[['user_profile_id']]
    df_user['user_id'] = range(2000, len(df_user)+2000)
    list_of_dfs.append({'name': 'user', 'dataframe': df_user})

    # role_profile_type
    df_role_profile_type = pd.DataFrame({'type': list(set(df_role_profile['role_profile'].values.tolist()))})
    df_role_profile_type['role_profile_type_id'] = range(1, len(df_role_profile_type)+1)
    list_of_dfs.append({'name': 'role_profile_type', 'dataframe': df_role_profile_type})

    # role_profile_type
    df_role_profile_table = df_full[['user_profile_id', 'role_profile']]
    df_role_profile_table = df_role_profile_table.merge(df_user, on='user_profile_id')
    df_role_profile_table = df_role_profile_table.merge(df_role_profile_type.rename(columns={"type": "role_profile"}),
                                                        on='role_profile')
    df_role_profile_table['role_profile_id'] = range(3000, len(df_role_profile_table)+3000)
    df_role_profile_table = df_role_profile_table[['role_profile_id', 'user_id', 'role_profile_type_id']]
    list_of_dfs.append({'name': 'role_profile', 'dataframe': df_role_profile_table})

    # email type = domain after the '@' symbol
    df_email_type = pd.DataFrame({'type': list(set(df_full[['email']].dropna()['email'].values.tolist()))})
    df_email_type['type'] = df_email_type['type'].map(lambda e: e.split("@")[1])
    df_email_type = df_email_type.drop_duplicates()
    df_email_type['email_type_id'] = range(1, len(df_email_type) + 1)
    list_of_dfs.append({'name': 'email_type', 'dataframe': df_email_type})

    # email
    df_email = df_full[['user_profile_id', 'email']]
    df_email = df_email.merge(df_user, on='user_profile_id')
    df_email = df_email.merge(df_role_profile_table, on='user_id')
    df_email['email_id'] = range(1, len(df_email) + 1)
    df_email = df_email.dropna()
    df_email['split_email'] = df_email['email'].map(lambda e: e.split("@")[1])
    df_email = df_email.merge(df_email_type.rename(columns={'type': 'split_email'}), on='split_email')
    df_email = df_email.rename(columns={'email': 'value'})
    df_email = df_email[['email_id', 'role_profile_id', 'email_type_id', 'value']]
    list_of_dfs.append({'name': 'email', 'dataframe': df_email})

    # address
    df_address = df_full[['id', 'street', 'city', 'state', 'zip_code', 'user_profile_id']]
    df_address = df_address.merge(df_user, on='user_profile_id')
    df_address = df_address.merge(df_role_profile_table, on='user_id')
    df_address = df_address.merge(df_role_profile_type, on='role_profile_type_id')
    df_address['address_id'] = range(1, len(df_address) + 1)
    df_address = df_address[['address_id', 'role_profile_id', 'street', 'city', 'state', 'zip_code']]
    list_of_dfs.append({'name': 'address', 'dataframe': df_address})

    # phone number type
    # phone number
    # To save time, I will not do the remaining tabels.
    # Quesitons: What would be a phone number type? Home or Cell? Which one would rank higher?

    # save data to parquet files
    for ddf in list_of_dfs:
        filename = f"{ddf['name']}.parquet"
        key = f"data/{ddf['name']}"

        # Validation here to find if parquet exists, use created date from uploaded parquet
        # find differences in dataframes and alter created data only
        df = ddf['dataframe']
        df['create_date'] = created_date
        df['created_by'] = 'admin'
        df['updated'] = created_date
        df['updated_by'] = 'admin'

        b4 = Boto4()
        b4.save_parquet_to_s3(df=df, key=key, filename=filename)


main()





