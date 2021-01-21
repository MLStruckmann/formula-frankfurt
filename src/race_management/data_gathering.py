import random
import time
from datetime import datetime, timedelta
import serial
import time

ser = serial.Serial('COM6', 9600)

def read_sensor():

    serial_inp = ser.readline()

    # serial read comes in format: Left:/signal/-Right:/signal/
    # example: Left:268-Right:229
    
    serial_txt = str(serial_inp)
    serial_stat = serial_txt.split("'")[1][4:][:-4]
    signal_driver1 = int(serial_stat.split('-')[0].split(':')[1])
    signal_driver2 = int(serial_stat.split('-')[1].split(':')[1])
    
    return signal_driver1, signal_driver2

# def generate_race_data(start_time, 
#                        lap_time_driver1, 
#                        lap_time_driver2):

#     time_difference = (datetime.now() - start_time).total_seconds()
    
#     if int(time_difference)%lap_time_driver1 == 0:
#         signal_driver1 = 35 + random.uniform(-2.0, 2.0)
#     else:
#         signal_driver1 = 350 + random.uniform(-5.0, +5.0)

#     if int(time_difference)%lap_time_driver2 == 0:
#         signal_driver2 = 35 + random.uniform(-2.0, 2.0)
#     else:
#         signal_driver2 = 350 + random.uniform(-5.0, +5.0)

#     time.sleep(0.2)

#     return signal_driver1, signal_driver2