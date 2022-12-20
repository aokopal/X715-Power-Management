from gpiozero import PWMOutputDevice, CPUTemperature
import time

PWM_PIN = 13
FREQUENCY = 2500

fan = PWMOutputDevice(PWM_PIN, frequency=FREQUENCY)
temp = CPUTemperature().temperature

while True:
    if (temp > 30):
        fan.value = 0.4

    if (temp > 50):
        fan.value = 0.5

    if (temp > 55):
        fan.value = 0.75

    if (temp > 60):
        fan.value = 0.9

    if (temp > 65):
        fan.value = 1.0

    if (temp < 30):
        fan.value = 0.0

    time.sleep(1)