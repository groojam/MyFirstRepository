import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT) #pin 임의 16번설정

p = GPIO.PWM(16, 50) #주파수 50Hz
p.start(0)

p.ChangeDutyCycle(3) #0도 방향으로 회전
sleep(1) #1초대기

p.ChangeDutyCycle(12) #180도 방향으로 회전
sleep(1)

p.ChangeDutyCycle(7.5) #90도 방향으로 회전
sleep(1)

while(1): # -1 입력될 때 까지 무한회전
    val = float(raw_input("input(3~7.5~12)= "))
    if val == -1:
        break
    p.ChangeDutyCycle(val)

p.stop()
GPIO.cleanup()
