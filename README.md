# AI Rotary Phone Project

## Schematics

Rotary Dial Wire | Function | RasPi Pico W Pin 
--- | --- | --- 
White | Pulse Contact | GP16 (input)
Red | Pulse Ground | GND
Blue | Off-Hook Contact | GP17 (input)
Brown | Off-Hook Ground | GND

Phone Speaker | Function | PAM8403 Amplifier 
--- | --- | --- 
Red | Speaker (+) | L OUT+ 
White | Speaker (-) | L OUT-

I2S DAC | Function | PAM8403 Amplifier 
--- | --- | --- 
LOUT | Left Audio Out | L IN 
ROUT | Right Audio Out | R IN
GND | Ground | GND

IS2DAC | Function | RasPi Pico W Pin  
--- | --- | --- 
BCK | Bit Clock | GP10 
WS | Word Select | GP11
DATA | Audio Data | GP9
VCC | Power | 3.3V
GND | Ground | GND
