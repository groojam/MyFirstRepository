import RPi.GPIO as GPIO
import time
rel1 = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(rel1, GPIO.OUT, initial = GPIO.LOW)

GPIO.output(rel1, GPIO.LOW)
print("on")
time.sleep(3)
#GPIO.output(rel1, GPIO.HIGH)
#print("off")

GPIO.cleanup()