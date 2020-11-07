import configparser
import os

config = configparser.ConfigParser()

config["DEFAULT"] = {"TimeZone": "UTC+01:00"}

# Azure Blob Storage Config
config["azure_blob_storage"] = {}
config["azure_blob_storage"]["key"] = "INSERT-KEY-HERE"
config["azure_blob_storage"]["connection_string"] = "INSERT-CONNECTION-STRING-HERE"

# Set config directory
config_path = os.path.join("config.ini")

with open(config_path, "w") as configfile:
    config.write(configfile)