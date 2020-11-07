import configparser
import os
from pathlib import Path
from azure.storage.blob import BlobServiceClient

# Define variables
container_name = "upload-test-6"
upload_folder = "/home/magnus/Downloads/upload_f"

# Read config
config = configparser.ConfigParser()
current_file_path = Path(os.path.abspath(__file__))
folder_directory = current_file_path.parent.parent
config_path = os.path.join(folder_directory,"azure-config.ini")
config.read(config_path)

# Assign variables from config
blob_account_url = config["azure_blob_storage"]["connection_string"]

# List all containers in storage account
blob_service_client = BlobServiceClient.from_connection_string(conn_str=blob_account_url)
all_containers = blob_service_client.list_containers()
container_list = []
print("\n\nContainers in storage account:")
for container in all_containers:
    print("\t" + container["name"])
    container_list.append(container["name"])

# List all files in upload folder
print("\nFiles in folder",upload_folder+":")
for file_name in os.listdir(upload_folder):
    print("\t"+file_name)

# Upload files
def upload_blob(upload_file_path):
    local_file_name = os.path.basename(upload_file_path)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    print("\t"+local_file_name)
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)

# Check if container exists
if container_name in container_list:
    print("\nContainer already exists")
else:
    print("\nContainer",container_name,"doesn't exist. Create new container")
    blob_service_client.create_container(container_name)

print("\nStart upload to",container_name)
print("Uploading from",upload_folder+":")

for file_name in os.listdir(upload_folder):
    file_path = os.path.join(upload_folder,file_name)
    upload_blob(file_path)

print("\n")