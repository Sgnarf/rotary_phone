import machine
import time

# Set up the hook pin with PULL_UP
HOOK_PIN = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)

def test_hook_pin():
    while True:
        hook_state = HOOK_PIN.value()  # Read the hook pin state
        
        if hook_state == 0:
            print("Off-hook")  # Phone is off-hook
        else:
            print("On-hook")  # Phone is on-hook

        time.sleep(0.5)  # Delay between checks for readability

# Start testing the hook pin state
test_hook_pin()
