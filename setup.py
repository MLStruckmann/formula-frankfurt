import configparser
import json
import os
from formula-frankfurt.image_transformation.image_transformation import calc_matrix

M = calc_matrix()

# test_M = str([[ 4.37936347e-01  1.14884857e+00 -3.09735413e+02]
#               [-3.98250557e-01  9.27410298e-01  7.26099746e+02]])

# Write Config File

config = {}

config["DEFAULT"] = {"TimeZone": "UTC+01:00"}

# Azure Blob Storage Config
config["azure_blob_storage"] = {}
config["azure_blob_storage"]["key"] = input('Enter Azure Blob Storage Key:')
config["azure_blob_storage"]["connection_string"] = input('Enter Azure Blob Storage Connection String:')

# Transformation Matrix
config["transformation_matrix"] = test_M
# Transformation points
# config["transformation_points"] = {}
# config["transformation_points"]["blue"] = "[1001, 1173]"
# config["transformation_points"]["red"] = "[1750, 1616]"
# config["transformation_points"]["yellow"] = "[3031, 1236]"

with open('config.json', 'w') as fp:
    json.dump(data, fp)