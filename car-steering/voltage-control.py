import serial
import time

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM6', 9600)

def set_resistance():
    user_input = input("\nType q / ... / o / terminate / LED: ")
    if user_input == "q":
        print("Set voltage to 0V")
        time.sleep(0.1) 
        ser.write(b'q') 
        set_resistance()
    elif user_input == "w":
        print("Set voltage to 1.5V")
        time.sleep(0.1)
        ser.write(b'w')
        set_resistance()
    elif user_input == "e":
        print("Set voltage to 2V")
        time.sleep(0.1)
        ser.write(b'e')
        set_resistance()
    elif user_input == "r":
        print("Set voltage to 2.5V")
        time.sleep(0.1)
        ser.write(b'r')
        set_resistance()
    elif user_input == "t":
        print("Set voltage to 3V")
        time.sleep(0.1)
        ser.write(b't')
        set_resistance()
    elif user_input == "z":
        print("Set voltage to 3.5V")
        time.sleep(0.1)
        ser.write(b'z')
        set_resistance()
    elif user_input == "u":
        print("Set voltage to 4V")
        time.sleep(0.1)
        ser.write(b'u')
        set_resistance()
    elif user_input == "i":
        print("Set voltage to 4.5V")
        time.sleep(0.1)
        ser.write(b'i')
        set_resistance()
    elif user_input == "o":
        print("Set voltage to 5V")
        time.sleep(0.1)
        ser.write(b'o')
        set_resistance()
    elif user_input =="terminate":
        print("Program exiting")
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
        set_resistance()  
    else:
        print("Invalid input. Enter q / ... / o / terminate / LED")
        set_resistance()

time.sleep(2) # wait for the serial connection to initialize

set_resistance()