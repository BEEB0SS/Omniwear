void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  display.begin(SSD1306_SWITCHCAPVCC, 0x3c);
  delay(100);
  display.clearDisplay();
  display.display();
  delay(100);

}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    String incomingString = Serial.readString();
    display.clearDisplay();
    display.setTextSize(1);
    display.setCursor(0,0);
    display.setTextColor(WHITE);
    display.println(incomingString);
    display.display();
    delay(1500);
  }

}
