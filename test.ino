bool x;
void setup() {
  Serial.begin(9600);
  pinMode(2,INPUT);
}

void loop() {
  x=digitalRead(2);
  if(x==1){
    Serial.println(x);
    delay(500);
  }
}
