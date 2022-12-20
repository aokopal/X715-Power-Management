from gpiozero import DigitalInputDevice
from time import sleep, time

TACH_PIN = 16

fan_tach = DigitalInputDevice(TACH_PIN)
pulse_count = 0

def pulse_callback():
    global pulse_count
    pulse_count += 1

fan_tach.when_activated = pulse_callback

while True:
    pulse_count = 0

    sleep_time = 1
    start_time = time()

    sleep(sleep_time)

    rpm = (pulse_count / sleep_time) * 60
    
    print("RPM: ", rpm)
