import requests
import smtplib


def send_email(message):
    sender = "pythonnotifications.max@gmail.com"
    password = "wtjvddloewrtnlbf"
    addressee = "maxkriv@mail.ru"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, addressee, message)

        return "The message sent successfully"
    except Exception as _ex:
        return f"{_ex}\nCheck your login or password"


url = ['http://185.221.152.176/', 'http://185.12.95.21/']

i = 0
n = 1

while i < len(url):
    try:
        response = requests.get(url[i], timeout=15)
    except requests.Timeout as e:
        print(str(e))
        message = str(e)
        send_email(message)
        break
    response_status = response.status_code
    if response_status == 200:
        print('Status of Node', n, '=', response_status, 'Success')
    else:
        print('Status of Node', n, '=', response_status, 'Mistake')
        message = F'Status of Node {n} = {response_status} Mistake'
        send_email(message)
        break
    i += 1
    n += 1