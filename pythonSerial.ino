const int pulsante = 9;   
const int ledPin =  12; 
const int ledPinc =  11; 

boolean buttonState;   
void setup() {

  pinMode(pulsante, INPUT_PULLUP); 
 pinMode(ledPin, OUTPUT);
  pinMode(ledPinc, OUTPUT);
  digitalWrite(ledPin,HIGH);
  Serial.begin(9600); 
}

void loop() {
  // Serial.println(buttonState);
  buttonState = digitalRead(pulsante);
    

  if (buttonState == LOW) {     
    digitalWrite(ledPin,HIGH);
    Serial.println("1");
 delay(18000);
  digitalWrite(ledPin,LOW);
   digitalWrite(ledPinc,HIGH);

  } 


  delay(10);

}

