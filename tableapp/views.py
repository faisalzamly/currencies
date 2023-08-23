import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout,login
from django.contrib.auth.decorators import login_required
from .models import *
num_table_bank = []  
num_table_gold = []  
num_table_price = []  
num_table_gold_dinar=[]
num_table_price_market = []  
list_name_table = []  
ind=0

from bs4 import BeautifulSoup
import os, requests

# os.system('pip install requests')
# os.system('pip install BeautifulSoup4')
# os.system('pip install bs4')
    


def script_table_bank():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
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
    for entry in data1[23]:
        numbers = re.findall(r'\((\d+)\)', entry)
        num_table_bank.append(numbers[0])
 
#3333#########################################################3

    url2 = 'https://www.cbi.iq/'
    r2 = requests.get(url2, headers=headers)
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
                    num_table_bank.append(cleaned_numeric_data[0])
    return num_table_bank
##########################################################################################3333333
def script_table_price():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

    url3 = "https://www.cbe.org.eg/ar/economic-research/statistics/cbe-exchange-rates"

    r3 = requests.get(url3, headers=headers)
    soup3 = BeautifulSoup( r3.content, 'html.parser')
    table3 = soup3.find('table', class_='table-comp layout-auto')
    if table3 is not None:
        rows = table3.find_all('tr')
        for row in rows[1:]:
            cells = row.find_all('td')
            if len(cells) >= 3:
                buy_rate = cells[2].text.strip()
                num_table_price.append(buy_rate)
    return num_table_price
##################################################################################################
def script_table_gold():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

    url4 = 'https://markets.businessinsider.com/commodities/gold-price'
    r4 = requests.get(url4, headers=headers)
    if r4.status_code == 200:
        soup4 = BeautifulSoup(r4.text, 'html.parser')
        
        price_div = soup4.find('div', class_='price-section__values')
        price_span = price_div.find('span', class_='price-section__current-value')
        num_table_gold.append(float(price_span.text.strip()))
    return num_table_gold
###########################3333###########################################################
def script_formatted_numbers(num_table_gold):
    gold_dollar=num_table_gold[0]
    num_table_gold.append(gold_dollar*32.1507466)
    num_table_gold.append(gold_dollar/31.1)
    gram_gold=num_table_gold[2]
    num_table_gold.append((gram_gold*22)/24)
    num_table_gold.append((gram_gold*21)/24)
    num_table_gold.append((gram_gold*18)/24)
    num_table_gold.append((gram_gold*14)/24)
    formatted_numbers = ["{:.2f}".format(num) for num in num_table_gold]
    return formatted_numbers


#######################################################################
def script_table_price_market():
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}

    url = 'https://sarf-today.com/currencies'
    r5 = requests.get(url, headers=headers)
    code_html5 = BeautifulSoup(r5.content, 'lxml')
    table = code_html5.find('table')
    rows = table.find_all('tr')

    for row in rows[1:]:  
        cells = row.find_all('strong')
        if len(cells) >= 1:  
            amount = cells[2].get_text(strip=True)
            num_table_price_market.append(float(amount))
    return num_table_price_market
# indices_to_remove = [3,12,13,15,16,17,18,19,21,22,23,24,25,26,27,28,29] 
# my_list = [item for index, item in enumerate(data5) if index not in indices_to_remove]
models1=table_bank.objects.all()
models2=table_price.objects.all()
models3=table_gold.objects.all()
models4=table_gold_dinar.objects.all()
models5=table_price_market.objects.all()
models6=name_table.objects.all()
models7=price_numper.objects.get(id=1)

for i in models6.values():
    list_name_table.append(i['name'])

num_table_price_market=script_table_price_market()
num_table_gold=script_table_gold()
num_table_price=script_table_price()
num_table_bank=script_table_bank()        
formatted_numbers=script_formatted_numbers(num_table_gold)

def index(request):
    

    
    list_name_table=[]
    for i in models6.values():
        list_name_table.append(i['name'])
    combined_data = zip(models1, num_table_bank)
    combined_data2 = zip(models2, num_table_price)
    combined_data3 = zip(models3, formatted_numbers)
    num_table_gold_dinar=[]
    for i in num_table_gold:
        num_table_gold_dinar.append("{:.2f}".format(i*models7.numper))
    combined_data4 = zip(models4, num_table_gold_dinar)
    combined_data5 = zip(models5, num_table_price_market)


    numper={
        'combined_data':combined_data,
        'combined_data2':combined_data2,
        'combined_data3':combined_data3,
        'combined_data4':combined_data4,
        'combined_data5':combined_data5,
        'list_name_table':list_name_table,
    }
    return render(request, 'index.html', numper)
    


def login1(request):
    if request.method == "POST":
        usernam = request.POST['username']
        passwor = request.POST['password']
        user = authenticate(username=usernam, password=passwor)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("/control")

        return redirect("/login")
    return render(request, "login.html")

@login_required(login_url='/login')
def Form1(request):
    if request.method == 'POST':
        name_table_form = request.POST['list_name_table0'] 
        models_name_table= name_table.objects.get(id=1)
        models_name_table.name =name_table_form
        list_name_table[0]=name_table_form
        models_name_table.save()
        for currency in models1:
            currency_name = request.POST.get(str(currency.id))  
            currency.name = currency_name
            currency.save()
        return redirect('/control')  

    else:
        return render(request, 'control.html')
@login_required(login_url='/login')
def Form2(request):
    if request.method == 'POST':
        name_table_form = request.POST['list_name_table1'] 
        models_name_table= name_table.objects.get(id=2)
        models_name_table.name =name_table_form
        list_name_table[1]=name_table_form
        models_name_table.save()
        for currency in models2:
            currency_name = request.POST.get(str(currency.id)) 
            currency.name = currency_name
            currency.save()
        return redirect('/control')  

    else:
        return render(request, 'control.html')
@login_required(login_url='/login')
def Form3(request):
    if request.method == 'POST':
        name_table_form = request.POST['list_name_table2'] 
        models_name_table= name_table.objects.get(id=3)
        models_name_table.name =name_table_form
        list_name_table[2]=name_table_form
        models_name_table.save()
        for currency in models3:
            currency_name = request.POST.get(str(currency.id))  
            currency.name = currency_name
            currency.save()
        return redirect('/control')  

    else:
        return render(request, 'control.html')
@login_required(login_url='/login')
def Form4(request):
    if request.method == 'POST':
        name_table_form = request.POST['list_name_table3'] 
        models_name_table= name_table.objects.get(id=4)
        models_name_table.name =name_table_form
        list_name_table[3]=name_table_form
        models_name_table.save()
        name_numper = request.POST['name_numper'] 
        models7.numper =float(name_numper)
        models7.save()
        for currency in models4:
            currency_name = request.POST.get(str(currency.id))  
            currency.name = currency_name
            currency.save()
       
        return redirect('/control')  

    else:
        return render(request, 'control.html')
@login_required(login_url='/login')
def Form5(request):
    if request.method == 'POST':
        name_table_form = request.POST['list_name_table4'] 
        models_name_table= name_table.objects.get(id=5)
        models_name_table.name =name_table_form
        list_name_table[4]=name_table_form
        models_name_table.save()
        for currency in models5:
            currency_name = request.POST.get(str(currency.id))  
            currency.name = currency_name
            currency.save()
        return redirect('/control')  

    else:
        return render(request, 'control.html')




@login_required(login_url='/login')
def Change_password(request):
    if request.user.is_superuser:
        if request.method == "POST":
            current_password = request.POST['current_password']
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_password']
            if new_password != confirm_password:
                passnotmatch = True
                return render(request, "Change_password.html", {'passnotmatch': passnotmatch})
            try:
                u = request.user
                if u.check_password(current_password):
                    u.set_password(new_password)
                    u.save()
                    alert = True
                    logout(request)
                    return render(request, "login.html", {'alert': alert})
                else:
                    currpasswrong = True
                    return render(request, "Change_password.html", {'currpasswrong': currpasswrong})
            except:
                return render(request, "Change_password.html")
        else:
            return render(request, "Change_password.html")
    else:
        return render(request, "index.html")
@login_required(login_url='/login')
def control(request):
    numper={
       
        'models1':models1,
        'models2':models2,
        'models3':models3,
        'models4':models4,
        'models5':models5,
        'list_name_table':list_name_table,
        'models7':models7,
       
        
    }
    return render(request, 'control.html', numper)

def Logout(request):
    logout(request)
    return redirect("/")