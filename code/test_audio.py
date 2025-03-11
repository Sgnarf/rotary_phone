from machine import Pin, I2S
import uasyncio as asyncio

# Define I2S pins
bck_pin = Pin(10)  # Bit Clock (BCK)
ws_pin = Pin(11)   # Word Select (LCK)
data_pin = Pin(9)  # Data (DIN)

# DAC Power Control
dac_power = Pin(2, Pin.OUT)  # GPIO2 controls DAC power

# Function to restart DAC
def reset_dac():
    print("Resetting DAC...")
    dac_power.value(0)  # Turn off DAC
    asyncio.sleep(0.5)  # Wait for power drain
    dac_power.value(1)  # Turn on DAC
    asyncio.sleep(0.5)  # Ensure it's stable

async def play_audio(filename):
    # Reset DAC before playing
    reset_dac()
    
    # Initialize I2S for audio output
    audio_out = I2S(
        0, sck=bck_pin, ws=ws_pin, sd=data_pin,
        mode=I2S.TX, bits=16, format=I2S.MONO, rate=16000, ibuf=20000
    )

    with open(filename, "rb") as f:
        f.seek(44)  # Skip WAV header
        while True:
            data = f.read(1024)
            if not data:
                break
            audio_out.write(data)
            await asyncio.sleep(0)

    print("Audio playback finished. Releasing I2S...")
    
    # Properly deinitialize I2S
    audio_out.deinit()

# Play a test file
asyncio.run(play_audio("test.wav"))
