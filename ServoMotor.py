import RPi.GPIO as GPIO #라즈베리파이 GPIO 핀을 쓰기위한 임포트
import time # 시간 간격으로 제어하는 임포트

def servoMotor(pin, degree, t):
    GPIO.setmode(GPIO.BOARD) #핀 번호를 보드기준으로 설정, BCM은 GPIO 번호로 호출
    GPIO.setup(pin, GPIO.OUT) #GPIO 통신할 핀 설정
    pwm = GPIO.PWM(pin, 50) #핀을 50Hz 주기로 설정

    pwm.start(3) #초기시작값
    time.sleep(t)

    pwm.ChangeDutyCycle(4) #괄호 값을 변경하면 해당위치로 변경함 (테스트를 위해 하나만 넣어봄)
    time.sleep(t)

    pwm.stop()
    GPIO.cleanup(pin)

servoMotor(16, 8, 1) #대충 16번핀이라 임의설정, (핀번호, 각도, 초) -> 8의 각도로 1초동안 실행
