import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL= 'https://www.amazon.in/Ocean-Storage-Additional-Exchange-Offers/dp/B07PTV49PJ/ref=pd_ybh_a_7?_encoding=UTF8&psc=1&refRID=ZMRVT79A69EF3MXAST6C'

headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[0:9])

if(converted_price < 41,999):
    send_mail()

print(converted_price)

print(title.strip())

if(converted_price < 41.999):
    send_mail()
 

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('js.king@gmail.com','iotunhceumlvjvai')

    subject = 'Price fell down!'
    body = 'check check the amazon link https://www.amazon.in/Ocean-Storage-Additional-Exchange-Offers/dp/B07PTV49PJ/ref=pd_ybh_a_7?_encoding=UTF8&psc=1&refRID=ZMRVT79A69EF3MXAST6C'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'js.king@gmail.com',
        'kingstondavid1998@gmail.com',
        msg
    )

print('Hey Email Has Been Sent ')

server.quit()

while(True):
    check_price()
    time.sleep(60*60)
