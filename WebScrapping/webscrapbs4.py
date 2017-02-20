import lxml
import bs4 as bs
import requests
#import urllib.request

sauce = requests.get("http://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bhopal")
sauce1 = requests.get("http://www.magicbricks.com/property-for-sale/residential-real-estate?price=Y&page=1&bar_propertyType_new=10002_10021_10022_10020&proptype=Multistorey-Apartment,Penthouse,Studio-Apartment&cityName=Bhopal&&price=Y&bar_propertyType_new=10002_10021_10022_10020&page=1&tab1Property=property&city=3808&category=S&source=projectSearch&searchType=5&mbTrackSrc=tabChange")
soup = bs.BeautifulSoup(sauce1.content, 'lxml')

for div in soup.find_all('div', class_='SRPriceB'):
    print(div.text)

#rows =soup.find_all('div',attrs={"class" : "SRPriceB"})
#rows1 =soup.find_all('div',attrs={"class" : "SRPPS"})
#print rows
print soup



