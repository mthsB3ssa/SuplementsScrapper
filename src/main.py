from bs4 import BeautifulSoup
import os
import requests
from twilio.rest import Client
import time

import pandas as pd
SHEET_ID = '1tp9kSgSWECcNJPkVJXFT103vd-InjSbZCIGjeRuK35E'
SHEET_NAME = 'Suples'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
for line in df["Links"]:
    print(line)

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

from_phone = os.getenv('TWILIO_FROM_PHONE')
to_phone = os.getenv('TO_PHONE')

def check_creatina():
    url = "https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824?busca=creatina"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    button_elements = soup.find_all('button') 
    creatinaInStock = False
    for button in button_elements:
        if button.has_attr('class') and 'botaoComprar' in button['class']:
            print("Button is available!")
            creatinaInStock = True  
    if creatinaInStock:
        client = Client(account_sid, auth_token)
        message = client.messages \
                    .create(
                            body="Creatina Disponível. Vem monstro",
                            from_=from_phone,
                            to=to_phone
                        )
        print(message.status)

while True:
    check_creatina()
    time.sleep(3600) #checa 1 vez por hora






