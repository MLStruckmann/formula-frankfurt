import configparser
import json
import os
from src.stream_analysis.image_transformation.image_transformation import calc_matrix

# Write Config File #
#####################

config = {}
config['session_name'] = input('Enter Session Name (Conference Etc.):')

# Azure Blob Storage Config
config['azure_cosmos_url'] = 'https://mls-dashboard-data.documents.azure.com:443/'
config['azure_cosmos_key'] = input('Enter Azure Cosmos Key:')
config['azure_cosmos_database_name'] = 'conference-data'
config['azure_cosmos_container_name'] = 'driver-data'

# Race management config
config['signal_limit'] = 100
config['buffer_time'] = 3
config['lap_number'] = 2

# Frontend config
config['aspect_ratio'] = '[1280,720]'
config['camera_aspect_ratio'] = [850,480]

# Image transformation config
reference_points_target = [[1194,370],[367,71],[96,546]] # blue, red, yellow
M = calc_matrix(reference_points_target)
config['transformation_matrix'] = M.tolist()

with open('src/config.json', 'w') as fp:
    json.dump(config, fp)

print('Setup Completed Successfully!')