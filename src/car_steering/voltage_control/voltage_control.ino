int sensorPinR = A0;
int sensorPinL = A1;

int sensorValueL = 0;
int sensorValueR = 0;
int output_pin = 5;

int incomingByte;            // a variable to read incoming serial data into

void setup() {
  Serial.begin(9600);
//  pinMode(output_pin, OUTPUT);
}

void loop() {
  sensorValueL = analogRead(sensorPinL);
  sensorValueR = analogRead(sensorPinR);

  Serial.print("Left:");
  Serial.print(sensorValueL);
  Serial.print("-");
  Serial.print("Right:");
  Serial.println(sensorValueR);

//  analogWrite(output_pin, 255);

  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    if (incomingByte == 'q') {
      analogWrite(output_pin, 160);
    }
    if (incomingByte == 'w') {
      analogWrite(output_pin, 140);
    }
    if (incomingByte == 'e') {
      analogWrite(output_pin, 120);
    }
}
}
