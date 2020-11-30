from functools import reduce
import random # for random driver name and random lap time
import string # only for random driver name
from datetime import datetime

class Driver:
    "Class for collecting driver lap data"

    # Initialize driver object
    def __init__(self, driver_name, raceid, conference_name, start_time):
        self.lap_count = 0
        self.lap_times = []
        self.driver_name = driver_name
        self.raceid = raceid
        self.conference_name = conference_name
        self.start_time = start_time
        self.time_stamp_last_lap = start_time

    # Calculate race metrics from driver data
    def calculate_metrics(self):
        self.fastest_lap = min(self.lap_times)
        average_lap = reduce(lambda a, b: a + b, self.lap_times) / len(self.lap_times)
        self.average_lap = round(average_lap,2)
        
    # Generate dictionary from driver data for upload to Azure cosmos
    def return_dict(self):
        driver_data = {}
        driver_data["raceid"] = self.raceid
        driver_data["driver_name"] = self.driver_name
        driver_data["average_lap"] = self.average_lap
        driver_data["fastest_lap"] = self.fastest_lap
        driver_data["number_of_laps"] = self.lap_count
        driver_data["conference_name"] = self.conference_name
        return driver_data

# Transform sensor data to relevant race data for both drivers (only ne input stream for both lap sensors) 
def collect_race_data_real(driver1, 
                           driver2, 
                           signal_driver1, 
                           signal_driver2,
                           lap_number):
    
    race_ongoing = True
    current_time = datetime.now()

    # Define range for lap sensor signal when sensor is activated
    lapSignal_lower, lapSignal_upper = 30, 40 # TODO REPLACE WITH VALUES FROM SETTINGS.JSON

    # Update data for driver1
    if lapSignal_lower < signal_driver1 < lapSignal_upper: # Check if lap sensor is activated
        if driver1.lap_count < lap_number: # Check if driver has already finished the race. If so, do not update race data.
            # Check if last active sensor signal is more than n seconds old:
            if (current_time - driver1.time_stamp_last_lap).total_seconds() > 3: # TODO REPLACE WITH VALUE FROM SETTINGS.JSON
                driver1.lap_count += 1
                driver1.lap_times.append((current_time - driver1.time_stamp_last_lap).total_seconds())
                driver1.time_stamp_last_lap = current_time
                print("\nLap updated for driver1")
                print("Lap count:\t",driver1.lap_count,"\nLap time:\t",driver1.lap_times)

    # Update data for driver2
    if lapSignal_lower < signal_driver2 < lapSignal_upper:
        if driver2.lap_count < lap_number:
            if (current_time - driver2.time_stamp_last_lap).total_seconds() > 3: # TODO REPLACE WITH VALUE FROM SETTINGS.JSON 
                driver2.lap_count += 1
                driver2.lap_times.append((current_time - driver2.time_stamp_last_lap).total_seconds())
                driver2.time_stamp_last_lap = current_time
                print("\nLap updated for driver2")
                print("Lap count:\t",driver2.lap_count,"\nLap time:\t",driver2.lap_times)

    # Check if both drivers have finished the race
    if driver1.lap_count >= lap_number and driver2.lap_count >= lap_number:
        race_ongoing = False # End race by ending race-loop

    return driver1, driver2, race_ongoing