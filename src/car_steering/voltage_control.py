import serial
import time
from datetime import datetime

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
#ser = serial.Serial('COM6', 9600)

def send_signal(ser,driver,driver_mode):
    # the voltage levels are defined in the Arduino sketch
    # ser.write(b'q') = 5.4 V
    # ser.write(b'w') = 6. V
    # ser.write(b'e') = 7 V

    current_time = datetime.now()
    lap_time = (current_time - driver.time_stamp_last_lap).total_seconds()
    #print(lap_time)
    if driver_mode == "easy":
        # constant speed (low)
        ser.write(b'q')

    elif driver_mode == "medium":
        # go faster on long straight
        if 2 < lap_time < 3:
            ser.write(b'w')
        else:
            ser.write(b'q')

    else:
        # go faster on long straight
        # go faster on remaining parts as well
        if 9 < lap_time < 13:
            ser.write(b'e')
        else:
            ser.write(b'w')