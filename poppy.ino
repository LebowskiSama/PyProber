
const int trigPin = 9;
const int echoPin =11;
const int solenoidPin = 7;

void setup() {
  // put your setup code here, to run once:
  pinMode(9,OUTPUT);
  pinMode(11,INPUT);
  pinMode(solenoidPin, OUTPUT);

  Serial.begin(9600);
}


void loop() {
  // put your main code here, to run repeatedly:
long distance;
long duration;
char SerialData;

if(Serial.available() > 0)
{
  SerialData = Serial.read();
  Serial.println(SerialData);
}

digitalWrite(trigPin, HIGH);
delayMicroseconds(2);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = (duration * 0.034) / 2;
  Serial.println(distance);
  delay(100);

if ( distance<=30  && SerialData == '1')
{
digitalWrite(solenoidPin, HIGH);
delay(5000);
//}
//else
//{
digitalWrite(solenoidPin, LOW);
//delay(500);
}
}
