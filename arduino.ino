#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
Adafruit_MPU6050 mpu;
void setup(void) {
  Serial.begin(9600);

  while (!mpu.begin()) {
    Serial.println("MPU6050 not connected!");
    delay(1000);
  }
  Serial.println("MPU6050 ready!");
}
sensors_event_t event;
void loop() {
  mpu.getAccelerometerSensor()->getEvent(&event);
  
  if(event.acceleration.x>3 and event.acceleration.y<3 and event.acceleration.y>-3)
  {
    Serial.println("s");
  }
  else if(event.acceleration.x<-3 and event.acceleration.y<3 and event.acceleration.y>-3)
  {
    Serial.println("w");
  }
  else if(event.acceleration.y>3 and event.acceleration.x<3 and event.acceleration.x>-3)
  {
    Serial.println("d");
  }
  else if(event.acceleration.y<-3 and event.acceleration.x<3 and event.acceleration.x>-3)
  {
    Serial.println("a");
  }
  else if(event.acceleration.x>3 and event.acceleration.y>3)
  {
    Serial.println("c");
  }
  else if(event.acceleration.x>3 and event.acceleration.y<-3)
  {
    Serial.println("z");
  }
  else if(event.acceleration.x<-3 and event.acceleration.y>3)
  {
    Serial.println("e");
  }
  else if(event.acceleration.x<-3 and event.acceleration.y<-3)
  {
    Serial.println("q");
  }
  delay(500);
}
