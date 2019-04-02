#!/usr/bin/env python

"""
Rotary Encoder
"""

import serial
import time


class WheelEncoder():
    def __init__(self):
        
        self.ser = serial.Serial('/dev/ttyACM0', 115200)
        self.ser.flushInput()

        self.poll_delay = 0.0166
        self.on = True
        self.velocity = 0.0


    def update(self):

         while(self.on):

            input = self.ser.readline()
            self.velocity = float(input)
            print('velocity (m/s):', self.velocity)

            time.sleep(self.poll_delay)

    def run_threaded(self):
        return self.velocity

    def shutdown(self):
        # indicate that the thread should be stopped
        self.on = False
        print('stopping Rotary Wheel Encoder')

        import RPi.GPIO as GPIO
        GPIO.cleanup()

