import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.co.uk/Logitech-Wireless-Lightweight-Programmable-compatible/dp/B07CGPZ3ZQ/ref=sr_1_4?crid=EXY296G3ZMIJ&dchild=1&keywords=logitech+mouse+wireless&qid=1623184887&s=computers&sprefix=logitech+mouse+%2Ccomputers%2C168&sr=1-4"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    # title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text() 
    converted_price = float(price[1:])

    if(converted_price <= 39):
        print("Email Sent!!!")
        send_email()

    print(converted_price)

def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("ugureren22@gmail.com", "rnbowsptdfjtweon")

    subject = "Logitech mouse price FELL bellow £37"
    body = "Check the amazon link https://www.amazon.co.uk/Logitech-Wireless-Lightweight-Programmable-compatible/dp/B07CGPZ3ZQ/ref=sr_1_4?crid=EXY296G3ZMIJ&dchild=1&keywords=logitech+mouse+wireless&qid=1623184887&s=computers&sprefix=logitech+mouse+%2Ccomputers%2C168&sr=1-4 "

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        "ugureren22@gmail.com",
        "ugureren22@gmail.com",
        msg.encode('utf-8')
    )

    server.quit()

check_price()

