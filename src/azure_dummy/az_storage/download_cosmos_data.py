import pandas as pd

def download_cosmos():

    return pd.read_csv(r'C:\Users\sdicarrera\Documents\formula-frankfurt\src\azure_dummy\az_storage\blob_dummy.csv', engine = 'python', sep=';')
