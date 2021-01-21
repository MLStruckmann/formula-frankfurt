from datetime import datetime
from race_management.data_gathering import read_sensor
from race_management.race_statistics import Driver, collect_race_data
from car_steering.voltage_control import send_signal
import random
import string
import serial

# Start race
print("------- Race started -------\n")
start_time = datetime.now()
lap_number = 5 # REPLACE WITH VALUE FROM CONFIG.JSON
ser = serial.Serial('COM6', 9600)

# Initialize driver data with Driver class

# REPLACE WITH VALUES FROM USER INPUT:
name_driver1, name_driver2 = ''.join(random.choice(string.ascii_lowercase) for i in range(4)),''.join(random.choice(string.ascii_lowercase) for i in range(4))
# Create unique IDs with race start time and driver names
raceid_driver1, raceid_driver2 = start_time.strftime("%Y%m%d-%H%M%S") + "_" + name_driver1, start_time.strftime("%Y%m%d-%H%M%S") + "_" + name_driver2
conference_name = "Datenkonferenz 1" # REPLACE WITH VALUE FROM CONFIG.JSON
driver1 = Driver(name_driver1, raceid_driver1, conference_name, start_time)
driver2 = Driver(name_driver2, raceid_driver2, conference_name, start_time)

race_ongoing = True # boolean value that ends race-loop when race is finished

while race_ongoing:

    signal_driver1, signal_driver2 = read_sensor(ser)

    # Transform sensor data to relevant race data for both drivers (only ne input stream for both lap sensors)
    driver1, driver2, race_ongoing = collect_race_data(driver1, 
                                                       driver2, 
                                                       signal_driver1, 
                                                       signal_driver2,
                                                       lap_number)

    auto_driver = "Left" # TODO insert which driver is autonomous from front end or config
    # if auto_driver not set to "Left" or "Right" no signal is sent; two human drivers can compete
    if auto_driver == "Left":
        send_signal(ser,driver1,"easy") # TODO insert driver mode from front end or config

    if auto_driver == "Right":
        send_signal(ser,driver2,"easy") # TODO insert driver mode from front end or config    
    
print("\n------- Race finished -------\n")
