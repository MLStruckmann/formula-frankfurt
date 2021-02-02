import pandas as pd

def download_cosmos():

    return pd.read_csv('src/azure_dummy/blob_dummy.csv', engine = 'python', sep=';')

def upload_cosmos(race_data):

    print('Upload not implemented in the dummy')
