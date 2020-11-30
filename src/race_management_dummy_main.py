from datetime import datetime
from race_management.data_gathering import generate_race_data
from race_management.race_statistics import Driver, collect_race_data_real
import random
import string

# Start race
print("------- Race started -------\n")
start_time = datetime.now()
lap_number = 5 # REPLACE WITH VALUE FROM CONFIG.JSON

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
    # Synthetically created sensor data (value around 30 = lap sensor active, value around 350 = lap sensor not active)
    signal_driver1, signal_driver2 = generate_race_data(start_time=start_time, 
                                                        lap_time_driver1=5, # lap time in seconds
                                                        lap_time_driver2=7) # race data print out true or false

    print("Driver 1:",signal_driver1,"\nDriver 2:",signal_driver2)

    # Transform sensor data to relevant race data for both drivers (only ne input stream for both lap sensors)
    driver1, driver2, race_ongoing = collect_race_data_real(driver1, 
                                                            driver2, 
                                                            signal_driver1, 
                                                            signal_driver2,
                                                            lap_number)

print("\n------- Race finished -------\n")
