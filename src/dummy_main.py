from race_management.start_race import collect_race_data, calculate_metrics
from azure_.az_storage.cosmos_data import upload_race, download_cosmos

#race_data = calculate_metrics(collect_race_data())
#upload_race(race_data)

print(download_cosmos())
