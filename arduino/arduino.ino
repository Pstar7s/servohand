#include <Servo.h>
Servo myServo;

void setup() {
  Serial.begin(9600);
  myServo.attach(9);
}

void loop() {
  if (Serial.available()) {
    int angle = Serial.parseInt();
    myServo.write(angle);
  }
}
