from maindash import get_config
from race_management.data_gathering import read_sensor
from car_steering.voltage_control import send_signal

import serial

from functools import reduce
from datetime import datetime
import json

class Driver:
    "Class for collecting driver lap data"

    # Initialize driver object
    def __init__(self, driver_name, raceid, conference_name, start_time):
        self.driver_name = driver_name
        self.raceid = raceid
        self.conference_name = conference_name
        self.start_time = start_time
        self.time_stamp_last_lap = start_time
        self.lap_count = 0
        self.lap_times = []
        self.fastest_lap = None
        self.average_lap = None

    # Calculate race metrics from driver data
    def calculate_metrics(self):
        self.fastest_lap = round(min(self.lap_times),2)
        average_lap = reduce(lambda a, b: a + b, self.lap_times) / len(self.lap_times)
        self.average_lap = round(average_lap,2)
        
    # Generate dictionary from driver data for upload to Azure Cosmos DB
    def to_dict(self, for_azure = False, as_json = False):

        driver_data = {}
        driver_data["raceid"] = self.raceid
        driver_data["driver_name"] = self.driver_name
        driver_data["lap_times"] = self.lap_times
        driver_data["average_lap"] = self.average_lap
        driver_data["fastest_lap"] = self.fastest_lap
        driver_data["number_of_laps"] = self.lap_count
        driver_data["conference_name"] = self.conference_name

        if not for_azure:

            del driver_data['number_of_laps']
            driver_data["lap_count"] = self.lap_count
            driver_data["start_time"] = self.start_time
            driver_data["time_stamp_last_lap"] = self.time_stamp_last_lap

        if as_json: return json.dumps(driver_data)

        return driver_data

def create_drivers(name_driver1, name_driver2, conference_name):

    start_time = datetime.now()

    raceid_driver1, raceid_driver2 = start_time.strftime("%Y%m%d-%H%M%S") + "_" + name_driver1, start_time.strftime("%Y%m%d-%H%M%S") + "_" + name_driver2
    driver1 = Driver(name_driver1, raceid_driver1, conference_name, start_time)
    driver2 = Driver(name_driver2, raceid_driver2, conference_name, start_time)

    return driver1, driver2

# Transform sensor data to relevant race data for both drivers (only ne input stream for both lap sensors) 
def collect_race_data(driver1, 
                      driver2, 
                      signal_driver1, 
                      signal_driver2,
                      lap_number,
                      signal_limit = 100,
                      buffer_time = 3):

    race_ongoing = True
    current_time = datetime.now()

    
    # Update data for driver1
    if signal_driver1 < signal_limit: # Check if lap sensor is activated
        if driver1.lap_count < lap_number: # Check if driver has already finished the race. If so, do not update race data.
            # Check if last active sensor signal is more than n seconds old:
            if (current_time - driver1.time_stamp_last_lap).total_seconds() > buffer_time:
                driver1.lap_count += 1
                driver1.lap_times.append((current_time - driver1.time_stamp_last_lap).total_seconds())
                driver1.time_stamp_last_lap = current_time
                print("\nLap updated for driver1")
                print("Lap count:\t",driver1.lap_count,"\nLap time:\t",driver1.lap_times)

    # Update data for driver2
    if signal_driver2 < signal_limit:
        if driver2.lap_count < lap_number:
            if (current_time - driver2.time_stamp_last_lap).total_seconds() > buffer_time:
                driver2.lap_count += 1
                driver2.lap_times.append((current_time - driver2.time_stamp_last_lap).total_seconds())
                driver2.time_stamp_last_lap = current_time
                print("\nLap updated for driver2")
                print("Lap count:\t",driver2.lap_count,"\nLap time:\t",driver2.lap_times)

    # Check if both drivers have finished the race
    if driver1.lap_count >= lap_number and driver2.lap_count >= lap_number:
        race_ongoing = False # End race by ending race-loop

    return driver1, driver2, race_ongoing

def run_race(driver1, driver2, lap_number, auto_driver = None, signal_limit = None, buffer_time = None):

    print("------- Race started -------\n")
    #start_time = datetime.now()
    ser = serial.Serial('COM6', 9600)

    race_ongoing = True # boolean value that ends race-loop when race is finished

    while race_ongoing:

        signal_driver1, signal_driver2 = read_sensor(ser)

        # Transform sensor data to relevant race data for both drivers (only ne input stream for both lap sensors)
        driver1, driver2, race_ongoing = collect_race_data(driver1, 
                                                        driver2, 
                                                        signal_driver1, 
                                                        signal_driver2,
                                                        lap_number = lap_number,
                                                        signal_limit = signal_limit,
                                                        buffer_time = buffer_time)

        #auto_driver = "Left" # TODO insert which driver is autonomous from front end or config
        # if auto_driver not set to "Left" or "Right" no signal is sent; two human drivers can compete
        if auto_driver == "L":
            send_signal(ser,driver1,"easy")

        if auto_driver == "R":
            send_signal(ser,driver2,"easy")
        
    return driver1, driver2