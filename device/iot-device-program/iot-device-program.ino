#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>

/* Set these to your desired credentials. */
const char* ssid = "";
const char* password = "";

int makeRequestHttpPost() {
  
  String host = "http://78440e12.ngrok.io/echo"; 
  
  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
 
    StaticJsonBuffer<300> JSONbuffer;   //Declaring static JSON buffer
    JsonObject& JSONencoder = JSONbuffer.createObject(); 
 
    //    JSONencoder["sensorType"] = "Temperature";
    // 
    //    JsonArray& values = JSONencoder.createNestedArray("values"); //JSON array
    //    values.add(20); //Add value to array
    //    values.add(21); //Add value to array
    
    JSONencoder["message"] = "HelloWorld";
 
    char JSONmessageBuffer[300];
    JSONencoder.prettyPrintTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));

    HTTPClient http; //Declare object of class HTTPClient
    
    Serial.println(host);
    http.begin(host);      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header
    
    int httpCode = http.POST(JSONmessageBuffer);   //Send the request JSONmessageBuffer
    if (httpCode == 200) {
      String payload = http.getString();  //Get the response payload
      Serial.println(payload);    //Print request response payload
      Serial.println(httpCode);   //Print HTTP return code
    } else {
      Serial.printf("[HTTP] POST... failed, error: %s\n", http.errorToString(httpCode).c_str());
    }
    http.end();  //Close connection

    return httpCode;
    
  } else {
 
    Serial.println("Error in WiFi connection");
    return 0;
  }  
}

int getLdrVoltage() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  
  // print out the value you read:
  Serial.println(voltage);
  return voltage;
}

void setup() {
  Serial.begin(9600);

  WiFi.begin(ssid, password);

  Serial.print("Connecting");
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {

  Serial.println("Run program!");

  Serial.printf("Get LDR Voltage..");
  getLdrVoltage();

  Serial.printf("Make HTTP POST..");
  makeRequestHttpPost();
 
  delay(20000);  //Send a request every 30 seconds
 
}
