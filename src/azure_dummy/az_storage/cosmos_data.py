import pandas as pd

def download_cosmos(key):

    return pd.read_csv('src/azure_dummy/az_storage/blob_dummy.csv', engine = 'python', sep=';')

def upload_cosmos(race_data,key):

    print('Upload not implemented in the dummy')
