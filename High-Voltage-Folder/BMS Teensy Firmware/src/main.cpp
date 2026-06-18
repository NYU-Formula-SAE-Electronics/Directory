#include <Arduino.h>
#include <math.h>
#include <FlexCAN_T4.h>

// Selector Signals
#define S_S0 2
#define S_S1 3
#define S_S2 4
// MUX Outputs to Teensy
#define MUX_D1 14
#define MUX_D2 15
#define MUX_D3 16
#define MUX_D4 17
#define MUX_D5 18

// CAN Object
FlexCAN_T4<CAN1, RX_SIZE_256, TX_SIZE_16> can1;

// ORION BMS SETTINGS
#define BASE_CAN_ID 0x80 // Default Orion Thermistor Module ID
#define MODULE_NUM 1     // 1 for Expansion Mod #1, 2 for Mod #2, etc.

float calculateTemperature(int rawADC) {
  if (rawADC <= 0 || rawADC >= 1023) return -99.0; 

  float r_s = 10000.0; 
  float rThermistor = r_s * ((float)rawADC / (1023.0 - rawADC));
  float nominalResistance = 10000.0; 
  float nominalTempK = 298.15;       
  float beta = 3984.0;               

  float one_over_standard = (1.0/nominalTempK);
  float one_over_beta = (1.0/beta);
  float r_over_r0 = (rThermistor/nominalResistance);
  float calculated_temp = (one_over_standard + (one_over_beta*(log(r_over_r0))));
  calculated_temp = (1.0/calculated_temp);

  return calculated_temp - 273.15;
}

// Orion Protocol Checksum: Sum of all bytes + ID + length, truncated to 8 bits
uint8_t calculateOrionChecksum(uint16_t id, uint8_t len, uint8_t b1, uint8_t b2, uint8_t b3) {
  uint32_t sum = id + len + b1 + b2 + b3;
  return (uint8_t)(sum & 0xFF);
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("Starting Orion BMS Thermistor Emulator");
  
  pinMode(S_S0,OUTPUT);
  pinMode(S_S1,OUTPUT);
  pinMode(S_S2,OUTPUT);
  
  pinMode(MUX_D1, INPUT);
  pinMode(MUX_D2, INPUT);
  pinMode(MUX_D3, INPUT);
  pinMode(MUX_D4, INPUT);
  pinMode(MUX_D5, INPUT);

  can1.begin();
  can1.setBaudRate(500000); // Ensure this matches your Orion CANBUS speed
}

void loop() {
  int8_t maxTemp = -128;
  int8_t minTemp = 127;
  
  int8_t validTemps[40]; 
  uint8_t validLocalIDs[40];
  int validCount = 0;
  bool faultPresent = false;

  // Read all MUX channels
  for (int channel = 0; channel < 8; channel++ ){
    digitalWrite(S_S0,bitRead(channel,0)); 
    digitalWrite(S_S1,bitRead(channel,1));
    digitalWrite(S_S2,bitRead(channel,2));
    
    // Reduced to 2ms. MUXes settle in microseconds. 20ms*8 = 160ms which is too slow!
    delay(2); 

    int raw_vals[] = { analogRead(MUX_D1), analogRead(MUX_D2), analogRead(MUX_D3), analogRead(MUX_D4), analogRead(MUX_D5) };
    
    for (int i = 0; i < 5; i++) {
      int local_id = (i * 8) + channel; // Assigns 0-39 based on MUX
      float temp_f = calculateTemperature(raw_vals[i]);
      
      if (temp_f > -50.0) { 
        int8_t temp_c = (int8_t)constrain(temp_f, -127, 127);
        validTemps[validCount] = temp_c;
        validLocalIDs[validCount] = local_id;
        validCount++;
        
        if (temp_c > maxTemp) maxTemp = temp_c;
        if (temp_c < minTemp) minTemp = temp_c;
      }
    }
  }

  // Fallback if no sensors work
  if (validCount == 0) {
    faultPresent = true;
    validTemps[0] = 100; // Force Orion to see overtemp fault
    validLocalIDs[0] = 0;
    validCount = 1;
    maxTemp = 100;
    minTemp = 100;
  }

  // --- ORION CAN BROADCAST PROTOCOL ---
  static bool sendHighNext = true;
  static int currentThermistorIndex = 0;

  if (currentThermistorIndex >= validCount) {
    currentThermistorIndex = 0;
  }

  int8_t currentTemp = validTemps[currentThermistorIndex];
  uint8_t currentLocalID = validLocalIDs[currentThermistorIndex];

  // Message 1: High/Low Broadcast (ID + 0)
  CAN_message_t msg0;
  msg0.id = BASE_CAN_ID + 0;
  msg0.len = 4;
  msg0.buf[0] = sendHighNext ? maxTemp : minTemp;
  msg0.buf[1] = faultPresent ? 1 : 0;
  
  // High/Low indicator calculation based on Expansion Module # 
  uint8_t baseIndicator = 5 + ((MODULE_NUM - 1) * 2); 
  msg0.buf[2] = sendHighNext ? (baseIndicator + 1) : baseIndicator; 
  msg0.buf[3] = calculateOrionChecksum(msg0.id, msg0.len, msg0.buf[0], msg0.buf[1], msg0.buf[2]);
  can1.write(msg0);

  // Message 2: Local Thermistor Loop (ID + 1)
  CAN_message_t msg1;
  msg1.id = BASE_CAN_ID + 1;
  msg1.len = 4;
  msg1.buf[0] = currentTemp;
  msg1.buf[1] = faultPresent ? 1 : 0;
  msg1.buf[2] = currentLocalID;
  msg1.buf[3] = calculateOrionChecksum(msg1.id, msg1.len, msg1.buf[0], msg1.buf[1], msg1.buf[2]);
  can1.write(msg1);

  // Message 3: Global/Relative Thermistor Loop (ID + 2)
  CAN_message_t msg2;
  msg2.id = BASE_CAN_ID + 2;
  msg2.len = 4;
  msg2.buf[0] = currentTemp;
  msg2.buf[1] = faultPresent ? 1 : 0;
  msg2.buf[2] = currentLocalID + ((MODULE_NUM - 1) * 80); // Module 2 starts at 80, etc 
  msg2.buf[3] = calculateOrionChecksum(msg2.id, msg2.len, msg2.buf[0], msg2.buf[1], msg2.buf[2]);
  can1.write(msg2);

  // Advance state for next cycle
  sendHighNext = !sendHighNext;
  currentThermistorIndex++;

  // Ensure our total loop time is ~100ms. 
  // Loop execution takes ~16ms, so we delay ~84ms. 
  delay(84); 
}