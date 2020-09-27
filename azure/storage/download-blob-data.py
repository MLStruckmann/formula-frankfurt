import configparser
import os
from pathlib import Path

config = configparser.ConfigParser()

# Read config
file_path = Path(os.path.abspath(__file__))
folder_directory = file_path.parent.parent
config_path = os.path.join(folder_directory,"azure-config.ini")
config.read(config_path)

# Config read example
print(config.sections())
print(config["azure_blob_storage"]["connection_string"])

'''import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

try:
    print("Azure Blob storage v" + __version__ + " - Python quickstart sample")
    # Quick start code goes here
except Exception as ex:
    print('Exception:')
    print(ex)'''