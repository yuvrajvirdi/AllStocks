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
        'percent': soup.find('div', {'class':'D(ib) Mend(20px)'}).find_all('span')[1].text,
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

def get_financials(stock_name):
    url = f'https://ca.finance.yahoo.com/quote/{stock_name}/financials?p={stock_name}'
    headers = {
        'User-agent': 'Mozilla/5.0',
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    labels = [
        soup.find('div',{'class':'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b)'}).find_all('span')[0].text,
        soup.find('div',{'class':'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b) Bgc($lv1BgColor)'}).find_all('span')[0].text,
        soup.find('div', {'class':'D(tbr) C($primaryColor)'}).find_all('div',{'class':'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(ib) Fw(b)'})[1].text,
    ]
    revenue = [
        int((soup.find('div',{'class':'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)'}).find_all('span')[0].text).replace(',','')),
        int((soup.find('div',{'D(tbr) fi-row Bgc($hoverBgColor):h'}).find_all('div',{'class':'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)'})[1].text).replace(',','')),
        int((soup.find('div',{'D(tbr) fi-row Bgc($hoverBgColor):h'}).find_all('div',{'class':'Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(100px)--pnclg D(tbc)'})[1].text).replace(',',''))
    ]
    cost = [
        int((soup.find_all('div',{'class':'D(tbr) fi-row Bgc($hoverBgColor):h'})[1].find_all('span')[2].text).replace(',','')),
        int((soup.find_all('div',{'class':'D(tbr) fi-row Bgc($hoverBgColor):h'})[1].find_all('span')[3].text).replace(',','')),
        int((soup.find_all('div',{'class':'D(tbr) fi-row Bgc($hoverBgColor):h'})[1].find_all('span')[4].text).replace(',',''))
    ]
    gross = [
        revenue[0]-cost[0],
        revenue[1]-cost[1],
        revenue[2]-cost[2]
    ]
    return [labels,revenue,cost,gross]

def get_holders(stock_name):
    url = f'https://ca.finance.yahoo.com/quote/{stock_name}/holders?p={stock_name}'
    headers = {
        'User-agent': 'Mozilla/5.0',
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    a = soup.find('table',{'class':'W(100%) M(0) BdB Bdc($seperatorColor)'}).find('tbody').find_all('tr',{'class':'BdT Bdc($seperatorColor)'})[0].find('td',{'class':'Py(10px) Ta(start) Va(m)'}).text
    b = soup.find('table',{'class':'W(100%) M(0) BdB Bdc($seperatorColor)'}).find('tbody').find_all('tr',{'class':'BdT Bdc($seperatorColor)'})[1].find('td',{'class':'Py(10px) Ta(start) Va(m)'}).text
    c = '% of Shares Held by Other'
    labels = [a,b,c]
    e = float((soup.find('table',{'class':'W(100%) M(0) BdB Bdc($seperatorColor)'}).find('tbody').find_all('tr',{'class':'BdT Bdc($seperatorColor)'})[0].find('td',{'class':'Py(10px) Va(m) Fw(600) W(15%)'}).text).replace('%',''))
    f = float((soup.find('table',{'class':'W(100%) M(0) BdB Bdc($seperatorColor)'}).find('tbody').find_all('tr',{'class':'BdT Bdc($seperatorColor)'})[1].find('td',{'class':'Py(10px) Va(m) Fw(600) W(15%)'}).text).replace('%',''))
    g = round(100-e-f,2)
    values = [e,f,g]
    return [labels,values]

def get_profile(stock_name):
    url = f'https://ca.finance.yahoo.com/quote/{stock_name}/profile?p={stock_name}'
    headers = {
        'User-agent': 'Mozilla/5.0',
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    profile_data={
        'logo': 'https://logo.clearbit.com/'+soup.find('p',{'D(ib) W(47.727%) Pend(40px)'}).find_all('a')[1].text,
        'sector': soup.find('p',{'class':'D(ib) Va(t)'}).find_all('span')[1].text,
        'industry': soup.find('p',{'class':'D(ib) Va(t)'}).find_all('span')[3].text,
        'employees': soup.find('p',{'class':'D(ib) Va(t)'}).find_all('span')[5].text,
    }
    return profile_data

def get_analytics(stock_name):
    url = f'https://ca.finance.yahoo.com/quote/{stock_name}/analysis?p={stock_name}'
    headers = {
        'User-agent': 'Mozilla/5.0',
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    growth = {
        'currentqtr':soup.find('td',{'data-reactid':'399'}).text,
        'nextqtr':soup.find('td',{'data-reactid':'406'}).text,
        'currentyr':soup.find('td',{'data-reactid':'413'}).text,
        'nextyr':soup.find('td',{'data-reactid':'420'}).text,
        'nextfiveyrs':soup.find('td',{'data-reactid':'427'}).text,
        'pastfiveyrs':soup.find('td',{'data-reactid':'434'}).text,
    }
    return growth
