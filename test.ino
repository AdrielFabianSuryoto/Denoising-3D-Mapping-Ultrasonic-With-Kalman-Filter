#include <Servo.h>

Servo servo1;
Servo servo2;
const int trigPin = 10;
const int echoPin = 9;

const int maxdist = 335;
const float mindist = 2.5;


double distance, duration;
int kaldist;

double kalman(double U){
  static const double R = 40;
  static const double H = 1.00;
  static double Q = 10;
  static double P = 1.0;
  static double U_hat = 0;
  static double K = 0;
  K = P*H/(H*P*H+R);
  U_hat += + K*(U-H*U_hat);
  P = (1-K*H)*P+Q;
  return U_hat;
}

void setup() {
  Serial.begin(9600);
  servo1.attach(6);
  servo2.attach(7);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  servo1.write(0);
  servo2.write(40);
}

void loop() {
 //moveServo();
  servo2.write(100);
  servo1.write(0);
//  //ultraSonic();
}

void moveServo() {
  for (int angle1 = 0; angle1 <= 40; angle1 += 5) {
    servo1.write(angle1);
    delay(1000);

    if (angle1 == 40) {
      servo1.write(0);
      delay(3000);

      if (angle1 == 40 && servo2.read() < 160) {
        servo2.write(servo2.read() + 10);
        delay(3000);
      } else {
        while (true) {
        }
      }
    }
    ultraSonic();
  }
}

void ultraSonic() {
  int angle1 =servo1.read();
  int angle2=servo2.read();
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);


  duration = pulseIn(echoPin, HIGH);
  int distance = (duration * 0.034) / 2;
  int kaldist = kalman(distance);

//  Serial.print("Distance (in cm): ");
//  Serial.println(distance);
//  Serial.print("Corrected distance (in cm): ");
//  Serial.println(kaldist);
//  delay(1000);
  
  
  Serial.print(angle1);
  Serial.print(',');
  Serial.print(angle2);
  Serial.print(',');
//  Serial.print(distance);
//  Serial.print(',');
  Serial.println(kaldist);

  delay(100);
}
