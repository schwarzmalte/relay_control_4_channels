int relay1 = 12; // Plug the relay into Digital Pin 
int relay2 = 11; // Plug the relay into Digital Pin 
int relay3 = 10; // Plug the relay into Digital Pin 
int relay4 = 9; // Plug the relay into Digital Pin 

void setup() {
  // put your setup code here, to run once:
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(1000);
  String back = turn_all_diodes_off();
  Serial.println("Write 1,2,3 or 4 to turn on relay 1,2,3 or 4. Write OFF to turn all relays off!");
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    String str = Serial.readString();
    Serial.println("You wrote: "+str);
    if (str == "1") {
      String back = turn_all_diodes_off();
      digitalWrite(relay1, LOW); // Turn the relay on
    }
    else if (str == "2") {
      String back = turn_all_diodes_off();
      digitalWrite(relay2, LOW); // Turn the relay on
    }
    else if (str == "3") {
      String back = turn_all_diodes_off();
      digitalWrite(relay3, LOW); // Turn the relay on
    }
    else if (str == "4") {
      String back = turn_all_diodes_off();
      digitalWrite(relay4, LOW); // Turn the relay on
    }else if (str == "OFF") {
      String back = turn_all_diodes_off();
    }
    else {
      Serial.println("Your input was not correct, try again!");
    }
  }
}

String turn_all_diodes_off(){
  digitalWrite(relay1, HIGH); // Turn the relay off
  digitalWrite(relay2, HIGH); // Turn the relay off
  digitalWrite(relay3, HIGH); // Turn the relay off
  digitalWrite(relay4, HIGH); // Turn the relay off
  return "OFF";
}