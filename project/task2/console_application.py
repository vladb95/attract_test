import urllib2
import json
class Parser:
    def get_current_weather_by_city(self,city='Odessa',country='ua'):
        url="http://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=78ff81d13bfe448fa634ac07c7a03741"%(city,country)
        content=urllib2.urlopen(url).read()
        print json.loads(content)
    def get_currency(self):
        url_finance="http://resources.finance.ua/ru/public/currency-cash.json"
        url_bitcoins="https://www.quandl.com/api/v1/datasets/BAVERAGE/USD.json?rows=1"
        bitcoins=json.loads(urllib2.urlopen(url_bitcoins).read())
        ukranian_banks=json.loads(urllib2.urlopen(url_finance).read())
        print bitcoins['name']+' '+str(bitcoins['data'][0][1])
        currency=ukranian_banks['organizations'][0]['currencies']['USD']
        print 'Ask: '+str(currency['ask'])+' Bid: '+str(currency['bid'])
parces=Parser()
print('1 - weather\n2 - currency\n anyting alse - exit')
menu_item=str(input('Choose menu item:'))
if menu_item=='1':
    city_name=str(input('Type city name:'))
    parces.get_current_weather_by_city(city=city_name)
elif menu_item=='2':
    parces.get_currency()
