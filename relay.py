import RPi.GPIO as GPIO
import time

#공기청정기 1, 제습기 2
#on/off 각각 1, 0
def relay(ctrl, onoff):
    #GPIO.HIGH / LOW => OFF = 1 ON = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    air_GPIO = 23 #공기 청정기
    dehumid_GPIO = 24 #제습기

    GPIO.setup(18,GPIO.OUT) #GROUND

    GPIO.setup(air_GPIO, GPIO.OUT)
    GPIO.setup(dehumid_GPIO, GPIO.OUT)
    GPIO.setup(window_GPIO, GPIO.OUT)
    
    #GPIO.HIGH / LOW => OFF = 1 ON = 0
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

    GPTO.cleanup()

if __name__ == '__main__':
    relay(1, 0) # 공기청정기 켜짐
    time.sleep(5)
    relay(1, 0) # 공기청정기 꺼짐

    time.sleep(2)

    relay(2, 0) # 제습기 켜짐
    time.sleep(5)
    relay(2, 0) # 제습기 꺼짐
