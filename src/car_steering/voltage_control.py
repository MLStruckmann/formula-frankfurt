import serial
import time
from datetime import datetime

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
#ser = serial.Serial('COM6', 9600)

def send_signal(ser,
                driver,
                driver_mode):

    # the voltage levels are defined in the Arduino sketch
    # ser.write(b'q') = 6.8 V
    # ser.write(b'w') = 7.3 V
    # ser.write(b'e') = 8 V

    if driver_mode == "easy":
        # constant speed (low)
        ser.write(b'q')

    elif driver_mode == "medium":
        # constant speed (medium)
        ser.write(b'w')

    else:
        # constant speed (hard)
        ser.write(b'e')
