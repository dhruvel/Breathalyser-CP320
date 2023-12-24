import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
TRIGGER_PIN=23
ECHO_PIN=24
HIGH_TIME=0.1
LOW_TIME=1-HIGH_TIME

GPIO.setup(TRIGGER_PIN,GPIO.OUT)
GPIO.setup(ECHO_PIN,GPIO.IN)
SPEED_OF_SOUND=330/float(1000000)

def getDistance(td):
	distance=SPEED_OF_SOUND*td/float(2)
	return distance

while True:
	GPIO.output(TRIGGER_PIN,GPIO.HIGH)
#	print 'Trigger HIGH'
	time.sleep(HIGH_TIME)
	GPIO.output(TRIGGER_PIN,GPIO.LOW)
#	print 'Trigger LOW'



	while GPIO.input(ECHO_PIN)==False:
# pulse is LOW
		pass


	starttime = datetime.datetime.now().microsecond
	while GPIO.input(ECHO_PIN)==True:
# pulse is HIGH
		pass

# pulse is LOW
	endtime = datetime.datetime.now().microsecond
	travel_time=endtime - starttime
	print (getDistance(travel_time))
	time.sleep(LOW_TIME)
