import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = 'https://www.elgiganten.se/product/datorer-kontor/datorer/laptop/acer-aspire-1-cel4128-14-barbar-dator-pure-silver/616149'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}

def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # title_tag = soup.find("div", class_="flex gap-2 flex-col pb-6").find("h1")

    price_tag = soup.find("div", class_="grid grid-cols-subgrid grid-rows-subgrid row-span-2 gap-1 items-end").find("span").get_text()
    converted_price = float(price_tag[0:5])
    
    if converted_price > 0:
        check_mail()

    print(converted_price)
    # print(title_tag.get_text(strip=True))

def check_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('sahand.omarzai@gmail.com', 'zjox guqo qkrl rzzy')
    
    subject = 'Notice Elgiganten!'
    body = 'Check the link for Elgiganten https://www.elgiganten.se/product/datorer-kontor/datorer/laptop/acer-aspire-1-cel4128-14-barbar-dator-pure-silver/616149'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'sahand.omarzai@gmail.com',
        'atticusfinsh@gmail.com',
        msg
    )
    print('Email has been sent!')
    
    server.quit()

while (True):
    check_price()
    time.sleep(60)