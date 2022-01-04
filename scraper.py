import requests
from bs4 import BeautifulSoup

def get_data(stock_name):
    url = f'https://ca.finance.yahoo.com/quote/{stock_name}'
    headers = {
        'User-agent': 'Mozilla/5.0',
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    stock_data = {
        'symbol': stock_name,
        'company': soup.find('h1', {'class':'D(ib) Fz(18px)'}).text,
        'price': soup.find('fin-streamer', {'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'change': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[0].text,
        'previous': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'PREV_CLOSE-value'}).text,
        'open': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'OPEN-value'}).text,
        'bid': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'BID-value'}).text,
        'ask': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'ASK-value'}).text,
        'daysrange': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'DAYS_RANGE-value'}).text,
        'weekrange': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'FIFTY_TWO_WK_RANGE-value'}).text, #52Week
        'volume': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'TD_VOLUME-value'}).text,
        'avgmonthvolume': soup.find('td', {'class':'Ta(end) Fw(600) Lh(14px)', 'data-test':'AVERAGE_VOLUME_3MONTH-value'}).text, #avg3monthvol
    }
    return stock_data