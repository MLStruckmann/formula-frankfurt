int sensorPinR = A0;         // lap time sensor left track
int sensorPinL = A1;         // lap time sensor right track

int sensorValueL = 0;        // lap time sensor signal left track
int sensorValueR = 0;        // lap time sensor signal right track
int output_pin = 5;          // send voltage signal to Arduino

int incomingByte;            // a variable to read incoming serial data into

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValueL = analogRead(sensorPinL);
  sensorValueR = analogRead(sensorPinR);

  // stream print out in one line because only one 
  // line per timestep can be analyzed in Python
  Serial.print("Left:");
  Serial.print(sensorValueL);
  Serial.print("-");
  Serial.print("Right:");
  Serial.println(sensorValueR);

  analogWrite(output_pin, 255);

  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer
    // voltage values per byte are defined in Python
    incomingByte = Serial.read();

    if (incomingByte == 'q') {
      analogWrite(output_pin, 165);
    }
    if (incomingByte == 'w') {
      analogWrite(output_pin, 155);
    }
    if (incomingByte == 'e') {
      analogWrite(output_pin, 145);
    }
    
}
}