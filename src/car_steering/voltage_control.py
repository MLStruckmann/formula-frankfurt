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

def set_voltage_manually():
    user_input = input("\nType q / ... / z / terminate / LED: ")
    if user_input == "q":
        print("q")
        time.sleep(0.1) 
        ser.write(b'q') 
        set_voltage_manually()
    elif user_input == "w":
        print("w")
        time.sleep(0.1)
        ser.write(b'w')
        set_voltage_manually()
    elif user_input == "e":
        print("e")
        time.sleep(0.1)
        ser.write(b'e')
        set_voltage_manually()
    elif user_input == "r":
        print("r")
        time.sleep(0.1)
        ser.write(b'r')
        set_voltage_manually()
    elif user_input == "t":
        print("t")
        time.sleep(0.1)
        ser.write(b't')
        set_voltage_manually()
    elif user_input == "z":
        print("z")
        time.sleep(0.1)
        ser.write(b'z')
        set_voltage_manually()
    elif user_input =="terminate":
        print("Terminate")
        time.sleep(0.1)
        ser.write(b'T')
        ser.close()
    elif user_input =="LED": 
        print("Do LED test")
        time.sleep(0.1)
        i = 0
        while i < 3:
            time.sleep(0.5)
            ser.write(b'X')
            time.sleep(0.5)
            ser.write(b'Y')
            i+=1
        set_voltage_manually()  
    else:
        print("Invalid input. Enter q / ... / o / terminate / LED")
        set_voltage_manually()

#time.sleep(2) # wait for the serial connection to initialize

#set_voltage_manually()
