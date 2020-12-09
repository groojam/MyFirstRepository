텔레그램으로 센서 값 전송하기
======================
* 텔레그램으로 센서 값을 전송하기 위한 python파일입니다.

### 설치한 것
* pip3 install python-telegram-bot --upgrade

***
### 소스코드
* git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
1. git clone으로 저장소를 다운로드를 합니다.
2. 다운로드한 저장소의 python-telegram-bot/examples 디렉토리 안의 echobot.py를 수정해 사용합니다.

***
### 실행 방법
* python3 transmission_SensorValue.py 로 실행합니다.
* 토큰을 넣었던 텔레그램 봇으로 메시지가 전송됩니다.
* 사용자가 텔레그램에서 /now 입력 시 센서 값이 전송되도록 합니다.
* 사용자가 텔레그램에서 /MicroDust 입력 시 인천 미추홀구에 있는 관측소에서 측정한 미세먼지 데이터가 전송됩니다.
* 사용자가 텔레그램에서 /help를 입력하면 "/now를 입력하시면 센서 값이 전송됩니다!"라는 안내 문구를 전송됩니다.
