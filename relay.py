import RPi.GPIO as GPIO

#GPIO.HIGH / LOW => OFF = 1 ON = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
air_GPIO = 23 #공기 청정기
dehumid_GPIO = 24 #제습기
window_GPIO = 25 #창문 모터

GPIO.setup(18,GPIO.OUT) #GROUND

GPIO.setup(air_GPIO, GPIO.OUT)
GPIO.setup(dehumid_GPIO, GPIO.OUT)
GPIO.setup(window_GPIO, GPIO.OUT)

#공기청정기 1, 제습기 2, 창문모터 3
#on/off 각각 1, 0
def relay(self, ctrl, onoff):
    if (ctrl == 1 and onoff == 0):
        GPIO.output(air_GPIO, GPIO.LOW)
        print("Air Purifier  OFF")
    elif (ctrl == 1 and onoff == 1):
        GPIO.output(air_GPIO, GPIO.HIGH)
        print("Air Purifier ON")
    elif (ctrl == 2 and onoff == 0):
        GPIO.output(dehumid_GPIO, GPIO.LOW)
        print("Dehumidifier  OFF")
    elif (ctrl == 2 and onoff == 1):
        GPIO.output(dehumid_GPIO, GPIO.HIGH)
        print("Dehumidifier  ON")
    elif (ctrl == 3 and onoff == 0):
        GPIO.output(window_GPIO, GPIO.LOW)
        print("Window OFF")
    elif (ctrl == 3 and onoff == 1):
        GPIO.output(window_GPIO, GPIO.HIGH)
        print("Window ON")
        
GPTO.cleanup()
