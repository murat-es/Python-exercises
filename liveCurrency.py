import requests
from bs4 import BeautifulSoup

url="https://www.doviz.com"
response=requests.get(url)

html_content=response.content
soup=BeautifulSoup(html_content,"html.parser")

currency=soup.find('div',{'class':'table table-narrow'})
unit=currency.findAll('a')
value=currency.findAll('td',{'class':'text-bold'})

values=[]
for i in range(0,len(value),2):
    i=(value[i].text)
    i=i.replace(",",".")
    values.append(float(i))

units=[]
for i in unit:
    i=i.text
    i=i.strip()
    units.append(i)

while(True):
    operation=int(input("1) USD-TRY\n2) EUR-TRY\n3) GBP-TRY\n4) EUR-USD\n5) GBP-USD\n6) GBP-EUR\n0) quit\n\nEnter operation:"))
    if(operation==1):
        print("1 USD equals {} TRY\n".format(values[0]))
    elif(operation==2):
        print("1 EUR equals {} TRY\n".format(values[1]))
    elif(operation==3):
        print("1 GBP equals {} TRY\n".format(values[2]))
    elif(operation==4):
        print("1 EUR equals {} USD\n".format(values[1]/values[0]))
    elif(operation==5):
        print("1 GPB equals {} USD\n".format(values[2]/values[0]))
    elif(operation==6):
        print("1 GBP equals {} EUR\n".format(values[2]/values[1]))
    elif(operation==0):
        print("Exiting...")
        break
    else:
        print("Invalid operation\n")