# from datetime import datetime
# from race_management.data_gathering import read_sensor
# from race_management.race_statistics import Driver, collect_race_data
# import random
# import string





# def run_race(lap_number, driver1, driver2):

#     race_ongoing = True

#     print("------- Race started -------\n")
#     start_time = datetime.now()
#     #lap_number = 5 # REPLACE WITH VALUE FROM CONFIG.JSON

#     while race_ongoing:
#         # Synthetically created sensor data (value around 30 = lap sensor active, value around 350 = lap sensor not active)
#         signal_driver1, signal_driver2 = generate_race_data(start_time=start_time, 
#                                                             lap_time_driver1=5, # lap time in seconds
#                                                             lap_time_driver2=7) # race data print out true or false

#         print("Driver 1:",signal_driver1,"\nDriver 2:",signal_driver2)

#         # Transform sensor data to relevant race data for both drivers (only ne input stream for both lap sensors)
#         driver1, driver2, race_ongoing = collect_race_data_real(driver1, 
#                                                                 driver2, 
#                                                                 signal_driver1, 
#                                                                 signal_driver2,
#                                                                 lap_number)

#     print("\n------- Race finished -------\n")