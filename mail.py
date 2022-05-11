import smtplib
from email.message import EmailMessage
import imghdr
import re

def sendEmail(addr): #유효하다면 전송, 유효하지 않다면 전송 X
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.+[a-zA-Z]{2,3}$" 
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

## MIME
## 1. 이메일을 만든다
message =  EmailMessage()
## 2. 이메일에 내용을 담는다
message.set_content("이메일 실습 중")
## 3. 발신자,  수신자를 설정한다
message["Subject"]  = "제목"
message["From"] = "limch9eri@gmail.com"
message["To"] = "limch9eri@gmail.com"

#############################################

#이미지 열기
with open("1.png", "rb") as image:
    image_file = image.read()

#여러가지 타입이 공존하는 이메일
image_type = imghdr.what('1', image_file) #이미지의 확장자 자동 인식
message.add_attachment(image_file, maintype="image", subtype=image_type)

#############################################

#1. SMTP 메일 서버를 연결한다
SMTP_SERVER =  "smtp.gmail.com"
SMTP_PORT  = 465
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)

#2. SMTP 메일 서버에 로그인한다
smtp.login("limch9eri@gmail.com",  "chaeri0306")

#3. SMTP 메일 서버로 메일을 보낸다
sendEmail("limch9eri@gmail.com")
smtp.quit()