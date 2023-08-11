import re
from django.shortcuts import render
# Create your views here.
from .models import *
num_table_bank = []  
num_table_gold = []  
num_table_price = []  
ind=0
try:
    from bs4 import BeautifulSoup
    import os, requests
except ImportError:
    os.system('pip install requests')
    os.system('pip install BeautifulSoup')
    os.system('pip install bs4')
    

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url = 'https://www.cbi.iq/currency_auction'
r = requests.get(url, headers=headers)
code_html = BeautifulSoup(r.content, 'lxml')
table1 = code_html.find('table')
rows = table1.find_all('tr')
data = []
for row in rows[1:]:  
    cells = row.find_all('span')
    if len(cells) >= 3:  
        description = cells[0].get_text(strip=True)
        amount = cells[2].get_text(strip=True)
        data.append((description, amount))
# total_amount = []
for _, amount in data:
    amount = amount.replace(',', '') 
    num_table_bank.append(amount)
    # total_amount.append(amount)###########
#############33333#######################################3
ul = code_html.find_all('ul')
data1 = []
for ul_element in ul[1:]:  
    li_elements = ul_element.find_all('li')
    numbers = []
    for li in li_elements:
        span_elements = li.find_all('span')
        if len(span_elements) >= 2:  
            number = span_elements[1].get_text(strip=True)
            numbers.append(number)
    data1.append(numbers)
def extract_numbers(text):
    numbers = []
    for word in text.split():
        try:
            number = int(word)
            numbers.append(number)
        except ValueError:
            pass
    return numbers
# extracted_numbers = []
for entry in data1[23]:
    numbers = re.findall(r'\((\d+)\)', entry)
    # extracted_numbers.extend(numbers)#########################
    num_table_bank.append(numbers[0])
# extracted_numbers = [int(num) for num in extracted_numbers]#################################
# num = [int(num) for num in extracted_numbers]
# print(num)
#3333#########################################################3
url2 = 'https://www.cbi.iq/'
r2 = requests.get(url2, headers=headers)
# numpers_currencies=[]
if r2.status_code == 200:
    soup1 = BeautifulSoup(r2.text, 'html.parser')
    table2 = soup1.find('table', class_='table-condensed')
    if table2:
        rows = table2.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            numeric_data = [cell.text.strip().replace(',', '') for cell in cells if all(c.isdigit() or c in [',', '.'] for c in cell.text.strip())]
            if numeric_data:
                cleaned_numeric_data = [data.strip('[]') for data in numeric_data]
                # numpers_currencies.append(cleaned_numeric_data)##########################
                num_table_bank.append(cleaned_numeric_data[0])
    else:
        print('لم يتم العثور على الجدول المطلوب.')

else:
    print('فشل في جلب محتوى الصفحة.')
##########################################################################################3333333
url3 = "https://www.cbe.org.eg/ar/economic-research/statistics/cbe-exchange-rates"

r3 = requests.get(url3, headers=headers)
soup3 = BeautifulSoup( r3.content, 'html.parser')
table3 = soup3.find('table', class_='table-comp layout-auto')
if table3 is not None:
    rows = table3.find_all('tr')
    # buy_rates = [] 
    for row in rows[1:]:
        cells = row.find_all('td')
        if len(cells) >= 3:
            buy_rate = cells[2].text.strip()
            # buy_rates.append(buy_rate)###################################
            num_table_price.append(buy_rate)
##################################################################################################
url4 = 'https://markets.businessinsider.com/commodities/gold-price'

r4 = requests.get(url4, headers=headers)
if r4.status_code == 200:
    soup4 = BeautifulSoup(r4.text, 'html.parser')
    
    price_div = soup4.find('div', class_='price-section__values')
    price_span = price_div.find('span', class_='price-section__current-value')
    # price_value = price_span.text.strip()##################
    num_table_gold.append(price_span.text.strip())
    # print(num_table_gold)
###########################3333###########################################################

def index(request):
    models1=table_bank.objects.all()
    models2=table_price.objects.all()
    models3=table_gold.objects.all()
    
    combined_data = zip(models1, num_table_bank)
    combined_data2 = zip(models2, num_table_price)
    combined_data3 = zip(models3, num_table_gold)
    numper={
       
        'combined_data':combined_data,
        'combined_data2':combined_data2,
        'combined_data3':combined_data3,
       
        
    }
    return render(request, 'index.html', numper)