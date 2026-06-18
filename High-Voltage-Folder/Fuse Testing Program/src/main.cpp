#include <Arduino.h>
#include <math.h>

// --- Pins ---
const int THERMISTOR_PIN = A0;
const int CURRENT_PIN = A1;
const int REF_PIN = A2;

// --- Timing ---
const unsigned long INTERVAL_MICROS = 5000; // 200Hz = 5000us
unsigned long lastSampleTime = 0;
float prevReading = 0.0;

// --- Constants ---
const float BETA = 3988;             
const float ROOM_TEMP_K = 298.15;    
const float RESISTOR_FIXED = 10000.0; 
const float THERM_NOMINAL = 10000.0; 

const float VOLT_DIVIDER_FACTOR = 1.5; // (1k + 2k) / 2k
const float V_REF_NOMINAL = 2.5;       // Internal reference of HO 100-S 
const float SENSITIVITY_LEM = 0.008;   // 8mV/A for HO 100-S 
unsigned long testStartTime = 0;
bool firstRun = true;
bool timerFlag = false;

float getStableRead(int pin) {
    long sum = 0;
    for(int i = 0; i < 16; i++) {
        sum += analogRead(pin);
    }
    return (float)sum / 16.0;
}

void setup() {
    Serial.begin(115200);
    analogReadResolution(12);
    analogReadAveraging(32); // Teensy 12-bit (0-4095)
    lastSampleTime = micros();
}

void loop() {
    if (firstRun) { 
        testStartTime = micros();
        firstRun = false;
        timerFlag = false;
         
    }
    if (micros() - lastSampleTime >= INTERVAL_MICROS) {
        lastSampleTime += INTERVAL_MICROS;
        

        // 1. Read Current (LEM HO 100-S-0100)
        float refI = getStableRead(REF_PIN);
        float rawI = getStableRead(CURRENT_PIN);
        float  calcIraw = (rawI - refI) - 10;
        
        // Current calculation: (Vout - Vref) / Sensitivity 
        float currentAmps = (calcIraw) / 6.0;
        int currentAmpsInt = round(currentAmps);
        if ((currentAmps - prevReading > 20) == true){
            timerFlag = true;
        }
        if ((prevReading - currentAmps > 20) == true){
            timerFlag = false;
        }
        // 2. Read Temperature (Vishay NTC 10k)
        float rawT = getStableRead(THERMISTOR_PIN);
        
        // Convert ADC bits to resistance
        // Formula for Thermistor on Bottom: R_ntc = R_fixed * (ADC_max / ADC_val - 1)
        float rNtc = RESISTOR_FIXED / ((4095.0 / rawT) - 1.0);

        // Steinhart-Hart Equation (Beta Formula)
        float steinhart;
        steinhart = rNtc / THERM_NOMINAL;          // (R/Ro)
        steinhart = log(steinhart);         // ln(R/Ro)
        steinhart /= BETA;                  // 1/B * ln(R/Ro)
        steinhart += 1.0 / ROOM_TEMP_K;          // + (1/To)
        steinhart = 1.0 / steinhart;        // Invert
        float tempC = steinhart - 273.15;   // Convert to Celsius

        float relativeTime = (micros() - testStartTime) / 1000000.0;

        
        Serial.print(relativeTime);
        Serial.print(",");
        Serial.print(currentAmpsInt);
        Serial.print(",");
        Serial.print(tempC);
        Serial.print(",");
        Serial.print(calcIraw);
        Serial.print(",");
        Serial.print(rawI);
        Serial.print(",");
        Serial.print(currentAmps);
        Serial.print("\n");


        

        float prev_reading = currentAmps;
    }
}