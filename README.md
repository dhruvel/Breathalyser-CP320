# Breathalyser-CP320
CP320 Final Project

This project is a Breathalyzer that uses a Raspberry Pi to control and monitor various components. The Breathalyzer consists of four main components:

1. **An Ultrasonic Sensor:** This is used to determine whether a user is close enough to the breathalyzer to take a reading.
   
2. **An MQ-3 Sensor:** This is used to measure the alcohol level in the user's breath.

3. **A Servo Motor:** This is used to indicate the user's alcohol level by moving a pointer to the appropriate position.

4. **An LED:** This is used to indicate when the user should breathe into the breathalyzer.

When the program first runs, it asks the user for a prompt "Press 's' to start". If the user presses 's', then the program runs; otherwise, it stops completely and exits.

Once the program starts, the ultrasonic sensor sends out an ultrasonic pulse and measures the time it takes for the pulse to bounce back to determine the distance of the object in front of it. This is used to determine whether the user is close enough to the breathalyzer to take a reading.

As the user gets closer, the LED brightness will increase. If the user is close enough, the LED will turn on with max brightness, indicating that the user should breathe into the breathalyzer. The MQ-3 sensor will then measure the alcohol level in the user's breath. The alcohol level is then mapped to a position for the servo motor to move to. The servo motor will move the pointer to the appropriate position, indicating the user's alcohol level.

If the user is far enough, the LED will remain off, and the MQ-3 sensor will not take a reading.

I have also used a PCF8591 ADC/DAC converter and an I2C interface to convert the analog signal from the MQ-3 sensor to a digital signal that can be read by the Raspberry Pi.

The Raspberry Pi is used to control all of these components and read the signals produced by the sensors. The code is written in Python and uses the RPi.GPIO and smbus libraries to control the GPIO pins and I2C interface, respectively.
