const int trackPin = 3;      // the pin that the track is connected to
const int ledPin = 13;       // the pin that the LED is attached to
int incomingByte;            // a variable to read incoming serial data into


void setup() {

  Serial.begin(9600);        // initialize serial communication
  pinMode(ledPin, OUTPUT);   // initialize the LED pin as an output
  pinMode(trackPin, OUTPUT); // initialize the track pin as an output
  
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a number, (ASCII 72), set voltage:
    if (incomingByte == 'q') {
      analogWrite(trackPin, 0);
    }
    if (incomingByte == 'w') {
      analogWrite(trackPin, 50);
    }
    if (incomingByte == 'e') {
      analogWrite(trackPin, 75);
    }
    if (incomingByte == 'r') {
      analogWrite(trackPin, 100);
    }
    if (incomingByte == 't') {
      analogWrite(trackPin, 125);
    }
    if (incomingByte == 'z') {
      analogWrite(trackPin, 150);
    }
    if (incomingByte == 'u') {
      analogWrite(trackPin, 175);
    }
    if (incomingByte == 'i') {
      analogWrite(trackPin, 200);
    }
    if (incomingByte == 'o') {
      analogWrite(trackPin, 225);
    }
    if (incomingByte == 'p') {
      analogWrite(trackPin, 255);
    }

    // if it's a capital T (ASCII 72), set resistance to 900 (step 90):
    if (incomingByte == 'T') {
      analogWrite(trackPin, 0);
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
