# Basic code to test PIR function
import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

sensor = Adafruit_DHT.DHT22
pin= 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN) #DHT22
GPIO.setup(17, GPIO.IN) #PIR
GPIO.setup(22, GPIO.OUT) #BUzzer

try:
    time.sleep(2) # to stabilize sensor
    while True:
	
	time.sleep(1)
	if GPIO.input(17):
            GPIO.output(22, True)
            time.sleep(0.5) #Buzzer turns on for 0.5 sec
            GPIO.output(22, False)
            print("Motion Detected...")
            time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay
	h,t=dht.Adafruit_DHT.read_retry(sensor,pin)
        print(h)
except:
    GPIO.cleanup()
