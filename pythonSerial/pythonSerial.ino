const int pulsante = 10;   
const int ledPin =  13; 


boolean buttonState = LOW;   
void setup() {
  
  pinMode(pulsante, INPUT); 
  
  Serial.begin(9600); 
}

void loop() {
 buttonState = digitalRead(pulsante);
  
 if (buttonState == LOW) {     
       
    Serial.println("1");
    delay(1000);
  } 
  if (Serial.read() == 2) {
    digitalWrite(ledPin,LOW);
  };
  
  delay(10);
  
}
