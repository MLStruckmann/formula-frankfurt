from azure.cosmos import CosmosClient
import json
import pandas as pd

url = "https://mls-dashboard-data.documents.azure.com:443/"
#key = "zRWAZ9FiwVtcZIqMhatuTf1knBYwQFYoYhXqJpfXQD9laT3mbVkJmeQsysAHUVq0QhMlMJZu40M8WDfOfgctVw==s"


def upload_cosmos(race_data, key):

    client = CosmosClient(url, credential=key)
    database_name = 'conference-data'
    database = client.get_database_client(database_name)
    container_name = 'driver-data'
    container = database.get_container_client(container_name)

    # upload race data
    for driver_data in race_data:
        container.upsert_item(driver_data)

def download_cosmos(key):

    client = CosmosClient(url, credential=key)
    database_name = 'conference-data'
    database = client.get_database_client(database_name)
    container_name = 'driver-data'
    container = database.get_container_client(container_name)

    fastest_drivers = pd.DataFrame(columns=["driver_name","average_lap","fastest_lap"])

    query_result = container.query_items(
        query='SELECT TOP 10 c.driver_name,c.average_lap,c.fastest_lap FROM c ORDER BY c.average_lap',
        enable_cross_partition_query=True)

    for item in query_result:
        fastest_drivers = fastest_drivers.append(item, ignore_index=True)

    return fastest_drivers
