import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 60)  # channel=12 frequency=60Hz
p.start(50)
time.sleep(5)
try:
    while True:
            p.ChangeDutyCycle(20)
            time.sleep(5)
            p.ChangeDutyCycle(100)
            time.sleep(5)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()