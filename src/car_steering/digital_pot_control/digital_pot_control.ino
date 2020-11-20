#include <X9C.h>                // X9C pot library

#define UD              10      // pot up/down mode pin
#define INC             11      // pot increment pin
#define CS              12      // pot chip select pin

const int ledPin = 13;      // the pin that the LED is attached to
int incomingByte;           // a variable to read incoming serial data into
X9C pot;                    // instantiate a pot controller

void setup() {

  pot.begin(CS, INC, UD);
  Serial.begin(9600);       // initialize serial communication
  pinMode(ledPin, OUTPUT);  // initialize the LED pin as an output
  
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a number, (ASCII 72), set resistance to number*10 in Ohms:
    if (incomingByte == 'q') {
      pot.setPot(0, false);
    }
    if (incomingByte == 'w') {
      pot.setPot(1, false);
    }
    if (incomingByte == 'e') {
      pot.setPot(2, false);
    }
    if (incomingByte == 'r') {
      pot.setPot(3, false);
    }
    if (incomingByte == 't') {
      pot.setPot(4, false);
    }
    if (incomingByte == 'z') {
      pot.setPot(5, false);
    }
    if (incomingByte == 'u') {
      pot.setPot(6, false);
    }
    if (incomingByte == 'i') {
      pot.setPot(7, false);
    }
    if (incomingByte == 'o') {
      pot.setPot(8, false);
    }
    if (incomingByte == 'p') {
      pot.setPot(9, false);
    }

    // if it's a capital T (ASCII 72), set resistance to 900 (step 90):
    if (incomingByte == 'T') {
      pot.setPot(90, false);
    }
    // if it's a capital X (ASCII 72), turn on the LED:
    if (incomingByte == 'X') {
      digitalWrite(ledPin, HIGH);
    }
    // if it's an Y (ASCII 76) turn off the LED:
    if (incomingByte == 'Y') {
      digitalWrite(ledPin, LOW);
    }
  }
}
