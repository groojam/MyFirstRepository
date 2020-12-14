import RPi.GPIO as GPIO
import time
from collections import deque



def window(whether):
  GPIO.setmode(GPIO.BCM)
  
  AIN1 = 12
  BIN1 = 16
  AIN2 = 20
  BIN2 = 21
  
  sig = deque([1,0,0,0])
  
  #rotate
  step = 500
  
  #direction
  dirc = 1

  
  GPIO.setup(AIN1, GPIO.OUT, initial = GPIO.LOW)
  GPIO.setup(BIN1, GPIO.OUT, initial = GPIO.LOW)
  GPIO.setup(AIN2, GPIO.OUT, initial = GPIO.LOW)
  GPIO.setup(BIN2, GPIO.OUT, initial = GPIO.LOW)

  # whether = input('창문을 여실거라면 open을 닫으실거라면 close를 입력해주세요')
  if whether == 'open':
      for cnt in range(0,step):
          GPIO.output(AIN1, sig[0])
          GPIO.output(BIN1, sig[1])
          GPIO.output(AIN2, sig[2])
          GPIO.output(BIN2, sig[3])
          time.sleep(0.01)
          sig.rotate(dirc)
      dirc = dirc*-1

  elif whether == 'close':
      dirc = dirc*-1 
      for cnt in range(0,step):
          GPIO.output(AIN1, sig[0])
          GPIO.output(BIN1, sig[1])
          GPIO.output(AIN2, sig[2])
          GPIO.output(BIN2, sig[3])
          time.sleep(0.01)
          sig.rotate(dirc)

  GPIO.cleanup()

if __name__ == '__main__':
  window()
