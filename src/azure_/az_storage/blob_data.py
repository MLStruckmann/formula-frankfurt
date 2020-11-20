from azure.storage.blob import BlobServiceClient
import os

def download_function(container_name,
                      blob_name_download,
                      download_folder,
                      blob_service_client):
    """
    This function downloads a specified blob from a specified Azure blob container.
    """
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name_download)
    download_file_path = os.path.join(download_folder,blob_name_download)
    print("\t"+blob_name_download)
    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

def download_blob_data(container_name,
                       blob_account_url,
                       download_folder="/home/magnus/Downloads",
                       blob_name=None):
    """
    This function iterates over all blobs in a container and calls 'download_function'.
    If a blob_name is specified the 'download_function' will only be called for that blob.
    """
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

    print("\nStart download from",container_name)
    print("Downloading to",download_folder+":")

    if blob_name == None:
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            download_function(container_name=container_name,
                              blob_name_download=blob.name,
                              download_folder=download_folder,
                              blob_service_client=blob_service_client)

    elif type(blob_name) == str:
        download_function(container_name=container_name,blob_name_download=blob_name)

    else:
        raise TypeError("blob_name was not type(str) or 'None'")

    print("\n")

def upload_function(container_name,
                    upload_file_path,
                    blob_service_client):
    """
    This function uploads a specified file to a specified Azure blob container.
    """             
    local_file_name = os.path.basename(upload_file_path)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    print("\t"+local_file_name)
    with open(upload_file_path, "rb") as data:
        blob_client.upload_blob(data)


def upload_blob_data(container_name,
                     blob_account_url,
                     upload_folder="/home/magnus/Downloads/upload_f"):
    """
    This function iterates over all files in a local folder and calls 'upload_function'.
    """
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
        upload_function(container_name=container_name,
                        upload_file_path=file_path,
                        blob_service_client=blob_service_client)

    print("\n")