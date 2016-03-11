import urllib2
import json
class Parser:
    def get_current_weather_by_city(self,city='Odessa',country='ua'):
        url="http://api.openweathermap.org/data/2.5/weather?q=%s,%s&appid=44db6a862fba0b067b1930da0d769e98"%(city,country)
        content=urllib2.urlopen(url).read()
        print json.loads(content)
    def get_currency(self):
        url_finance="http://resources.finance.ua/ru/public/currency-cash.json"
        url_bitcoins="https://www.quandl.com/api/v1/datasets/BAVERAGE/USD.json?rows=1"
        bitcoins=json.loads(urllib2.urlopen(url_bitcoins).read())
        #bitcoins=urllib2.urlopen(url_bitcoins).read()
        ukranian_banks=json.loads(urllib2.urlopen(url_finance).read())
        print bitcoins['name']+' '+str(bitcoins['data'][0][1])
        #print ukranian_banks
weather=Parser()
#city_name=input('Type city name:')
#weather.get_current_weather_by_city(city=city_name)
weather.get_currency()
