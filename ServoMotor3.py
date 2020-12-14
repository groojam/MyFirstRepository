import RPi.GPIO as GPIO
from time import sleep

def window():
  pin = 12 # pwm 핀 18번

  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pin, GPIO.OUT)
  p = GPIO.PWM(pin, 50) #핀을 50Hz 주기로 설정
  p.start(0)

  whether = input('창문을 여실거라면 open을 닫으실거라면 close를 입력해주세요')
  if whether == 'open':
    p.ChangeDutyCycle(2.5)
    sleep(0.5)

  elif whether == 'close':
    p.ChangeDutyCycle(12.5)
    sleep(0.5)

  p.stop()
  GPIO.cleanup()

if __name__ == '__main__':
  window()
