import machine
import time

PULSE_PIN = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    print(PULSE_PIN.value())  # Print pulse signal in real time
    time.sleep(0.1)  # Short delay for readability
