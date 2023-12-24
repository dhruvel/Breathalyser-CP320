import smbus
import time
address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)
while True:
	#A2 is the input detecting the MQ-3 output
	bus.write_byte(address,A2)
	value = bus.read_byte(address)
	print(value)
	time.sleep(0.1)
