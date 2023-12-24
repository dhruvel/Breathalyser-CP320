import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)  # channel=12 frequency=60Hz
p.start(0)
time.sleep(5)
try:
    while True:
            p.ChangeDutyCycle(10)
            time.sleep(5)
            p.ChangeDutyCycle(5)
            time.sleep(5)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
