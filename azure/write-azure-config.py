import configparser
import os

config = configparser.ConfigParser()

config["DEFAULT"] = {"TimeZone": "UTC+01:00"}

# Azure Blob Storage Config
config["azure_blob_storage"] = {}
config["azure_blob_storage"]["key"] = "INSERT-KEY-HERE"
config["azure_blob_storage"]["connection_string"] = "INSERT-CONNECTION-STRING-HERE"

# Set config directory
file_path = os.path.abspath(__file__)
folder_directory = os.path.dirname(file_path)
config_path = os.path.join(folder_directory,"azure-config.ini")

with open(config_path, "w") as configfile:
    config.write(configfile)