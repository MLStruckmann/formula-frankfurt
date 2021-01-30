from azure.cosmos import CosmosClient
import json
import pandas as pd
from maindash import get_config

config = get_config()
url = config["azure_cosmos_url"]
key = config["azure_cosmos_key"]
database_name = config["azure_cosmos_database_name"]
container_name = config["azure_cosmos_container_name"]

def upload_cosmos(race_data):

    client = CosmosClient(url, credential=key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    # upload race data
    for driver_data in race_data:
        if driver_data["driver_name"] not in ['easy', 'medium', 'hard']:
            container.upsert_item(driver_data)

def download_cosmos():
    client = CosmosClient(url, credential=key)
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)
    fastest_drivers = pd.DataFrame(columns=["driver_name","conference_name","average_lap","fastest_lap"])

    query_result = container.query_items(
        query='SELECT TOP 10 c.driver_name,c.conference_name,c.average_lap,c.fastest_lap FROM c ORDER BY c.average_lap',
        enable_cross_partition_query=True)

    try:
        for item in query_result:
            fastest_drivers = fastest_drivers.append(item, ignore_index=True)
    except:
        raise Exception("Azure download error. Check connection URL and key")

    return fastest_drivers
