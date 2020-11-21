from functools import reduce
import random # for random driver name and random lap time
import string # only for random driver name
from datetime import datetime

def collect_race_data():

    driver1_data = {"lap_times":[random.uniform(15.0, 30.0),random.uniform(15.0, 30.0),random.uniform(15.0, 30.0),random.uniform(15.0, 30.0)]}
    driver2_data = {"lap_times":[random.uniform(15.0, 30.0),random.uniform(15.0, 30.0),random.uniform(15.0, 30.0),random.uniform(15.0, 30.0)]}
    race_data = [driver1_data,driver2_data]

    return race_data

def average(lst): 
    return reduce(lambda a, b: a + b, lst) / len(lst)

def calculate_metrics(race_data, conference):

    time_stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    for driver_data in race_data:
        driver_name_random = ''.join(random.choice(string.ascii_lowercase) for i in range(4))
        driver_data["raceid"] = time_stamp + "_" + driver_name_random
        driver_data["driver_name"] = driver_name_random
        driver_data["average_lap"] = round(average(driver_data["lap_times"]),2)
        driver_data["fastest_lap"] = min(driver_data["lap_times"])
        driver_data["number_of_laps"] = len(driver_data["lap_times"])
        driver_data["conference_name"] = conference
    return race_data