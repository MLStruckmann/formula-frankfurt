import random
import time
from datetime import datetime, timedelta
import time

def read_sensor(ser):

    serial_inp = ser.readline()

    # serial read comes in format: Left:/signal/-Right:/signal/
    # example: Left:268-Right:229
    
    serial_txt = str(serial_inp)
    serial_stat = serial_txt.split("'")[1][4:][:-4]
    signal_driver1 = int(serial_stat.split('-')[0].split(':')[1])
    signal_driver2 = int(serial_stat.split('-')[1].split(':')[1])
    
    return signal_driver1, signal_driver2