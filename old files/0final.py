import RPi.GPIO as GPIO
import time
import datetime
import smbus

# Pin configuration for ultrasonic sensor
GPIO.setmode(GPIO.BCM)
TRIGGER_PIN = 23
ECHO_PIN = 24
HIGH_TIME = 0.1
LOW_TIME = 1 - HIGH_TIME
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
SPEED_OF_SOUND = 330 / float(1000000)

# Pin configuration for servo motor
SERVO_PIN = 12
GPIO.setup(SERVO_PIN, GPIO.OUT)
p = GPIO.PWM(SERVO_PIN, 50)  # channel=12 frequency=50Hz
p.start(0)

# Pin configuration for MQ-3 sensor
address = 0x48
A2 = 0x42
bus = smbus.SMBus(1)

# Pin configuration for LED
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to get the distance from the ultrasonic sensor
def getDistance(td):
    distance = SPEED_OF_SOUND * td / float(2)
    return distance

try:
    # Loop to continuously monitor the components
    while True:
        # Measure the distance from the ultrasonic sensor
        GPIO.output(TRIGGER_PIN, GPIO.HIGH)
        time.sleep(HIGH_TIME)
        GPIO.output(TRIGGER_PIN, GPIO.LOW)
        while GPIO.input(ECHO_PIN) == False:
            pass
        starttime = datetime.datetime.now().microsecond
        while GPIO.input(ECHO_PIN) == True:
            pass
        endtime = datetime.datetime.now().microsecond
        travel_time = endtime - starttime
        distance = getDistance(travel_time)

        print("Distance: " + str(distance) + "m")
        # Check if the user is close enough to the breathalyzer
        if distance < 0.05:
            # Turn on the LED to indicate the user should breathe into the MQ-3 sensor
            GPIO.output(LED_PIN, True)

            # Read the alcohol percentage from the MQ-3 sensor
            bus.write_byte(address, A2)
            alcohol_percentage = bus.read_byte(address)

            # Map the alcohol percentage to a servo position
            if alcohol_percentage < 50:
                servo_position = 0
            elif alcohol_percentage < 100:
                servo_position = 5
            else:
                servo_position = 10

            # Move the servo to the appropriate position
            p.ChangeDutyCycle(servo_position)
        else:
            # Turn off the LED if the user is not close enough to the breathalyzer
            GPIO.output(LED_PIN, False)

        time.sleep(LOW_TIME)
except KeyboardInterrupt:
    pass
    
GPIO.cleanup()
