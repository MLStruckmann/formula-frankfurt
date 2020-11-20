import configparser
import os
from pathlib import Path
from azure.storage.blob import BlobServiceClient

# Define variables
container_name = "upload-test-3"
blob_name = None # set blob_name (str) if you only want to download a single file from specified container
download_folder = "/home/magnus/Downloads"

# Read config
config = configparser.ConfigParser()
config.read("config.ini")

# Assign variables from config
blob_account_url = config["azure_blob_storage"]["connection_string"]

# List all containers in storage account
blob_service_client = BlobServiceClient.from_connection_string(conn_str=blob_account_url)
all_containers = blob_service_client.list_containers()
print("\n\nContainers in storage account:")
for container in all_containers:
    print("\t" + container["name"])

# List files in container
container_client = blob_service_client.get_container_client(container_name)
blob_list = container_client.list_blobs()
print("\nFiles in container",container_name+":")
for blob in blob_list:
    print("\t" + blob.name)

# Download files
def download_blob(blob_name_download):
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name_download)
    download_file_path = os.path.join(download_folder,blob_name_download)
    print("\t"+blob_name_download)
    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

print("\nStart download from",container_name)
print("Downloading to",download_folder+":")

if blob_name == None:
    blob_list = container_client.list_blobs()
    for blob in blob_list:
        download_blob(blob_name_download=blob.name)

elif type(blob_name) == str:
    download_blob(blob_name_download=blob_name)

else:
    raise TypeError("blob_name was not type(str) or 'None'")

print("\n")