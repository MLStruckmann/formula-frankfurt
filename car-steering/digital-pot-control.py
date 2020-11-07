import serial
import time

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM6', 9600)

def set_resistance():
    user_input = input("\nType q / ... / o / terminate / LED: ")
    if user_input == "q":
        print("Set resistance to 30 Ohms")
        time.sleep(0.1) 
        ser.write(b'q') 
        set_resistance()
    elif user_input == "w":
        print("Set resistance to 40 Ohms")
        time.sleep(0.1)
        ser.write(b'w')
        set_resistance()
    elif user_input == "e":
        print("Set resistance to 49 Ohms")
        time.sleep(0.1)
        ser.write(b'e')
        set_resistance()
    elif user_input == "r":
        print("Set resistance to 58 Ohms")
        time.sleep(0.1)
        ser.write(b'r')
        set_resistance()
    elif user_input == "t":
        print("Set resistance to 67 Ohms")
        time.sleep(0.1)
        ser.write(b't')
        set_resistance()
    elif user_input == "z":
        print("Set resistance to 76 Ohms")
        time.sleep(0.1)
        ser.write(b'z')
        set_resistance()
    elif user_input == "u":
        print("Set resistance to 85 Ohms")
        time.sleep(0.1)
        ser.write(b'u')
        set_resistance()
    elif user_input == "i":
        print("Set resistance to 94 Ohms")
        time.sleep(0.1)
        ser.write(b'i')
        set_resistance()
    elif user_input == "o":
        print("Set resistance to 103 Ohms")
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