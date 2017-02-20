from selenium import webdriver
import time, json
import lxml
import re
import bs4 as bs
from collections import defaultdict
from selenium.common.exceptions import TimeoutException  
from selenium.common.exceptions import NoSuchElementException, WebDriverException, ElementNotVisibleException

chrome_path = "C:\Users\Tausif\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.get("http://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&cityName=Bhopal")
time.sleep(2)
#driver.find_element_by_xpath("""//img[@ src='http://cdn.staticmb.com/images/iconCloseLeaderBoard.png']""").click()
#input = driver.find_element_by_xpath("""//*[@id="autoSuggestInputDivkeyword"]""")
#input.clear()
#inputElement = driver.find_element_by_xpath("""//*[@id="keyword"]""")
#inputElement.send_keys('BHOPAL')
#driver.find_element_by_xpath("""//*[@id="btnPropertySearch"]""").click()
#time.sleep(2)
#driver.find_element_by_xpath("""//*[@id="viewMoreButton"]/a""").click()
#time.sleep(25)
#driver.find_element_by_xpath("""//*[@id="viewMoreButton"]/a""").click()
#time.sleep(25)
#driver.find_element_by_xpath("""//*[@id="viewMoreButton"]/a""").click()
#time.sleep(20)
#driver.find_element_by_xpath("""//*[@id="viewMoreButton"]/a""").click()
#time.sleep(20)
#driver.find_element_by_xpath("""//*[@id="viewMoreButton"]/a""").click()
#time.sleep(20)

retry = 0
while retry < 0:
    try:
        driver.find_element_by_xpath("""//img[@ src='http://cdn.staticmb.com/images/iconCloseLeaderBoard.png']""").click()
    except Exception, e:#NoSuchElementException, WebDriverException, ElementNotVisibleException:
        print ('Adv')
        print retry
    try:
        driver.find_element_by_xpath("""//*[@id="viewMoreButton"]/a""").click()
        retry = retry + 1
    except Exception, e:#NoSuchElementException, WebDriverException, ElementNotVisibleException:
        print ('ViewButton')
        print retry
        
Price = []
for elem in driver.find_elements_by_xpath("""//div[@class='SRPriceB']"""):
    #print elem.text
    Price.append(str(elem.text))
print (Price)

SqPrice = []
for elem in driver.find_elements_by_xpath("""//div[@class='SRPPS']"""):
    #print elem.text
    SqPrice.append((elem.text).encode('utf-8'))
print (SqPrice)

PropBrief = []
for elem in driver.find_elements_by_xpath("""//div[@class='proBrf']"""):
    #print elem.text
    PropBrief.append((elem.text).encode('utf-8'))
print (PropBrief)

AreaValue = []
for elem in driver.find_elements_by_xpath("""//label[@class='areaValue']"""):
    #print elem.text
    AreaValue.append((elem.text).encode('utf-8'))
print (AreaValue)






Final_Dict = defaultdict(dict)
j = 0
for i in Price:
    Final_Dict[j]['Sale_Price'] = Price[j]
    Final_Dict[j]['Sq_Price'] = SqPrice[j]
    Final_Dict[j]['Prop_Brief'] = PropBrief[j]
    Final_Dict[j]['Area_Value'] = AreaValue[j]
    #print((re.search(r'\d,\d+|\d+', SqPrice[j]).group()).replace(',',''))
    print(float(re.search(r'\d+.\d+|\d+', Price[j]).group()))
    Final_Dict[j]['Sq_Price_Int'] = int((re.search(r'\d,\d+|\d+', SqPrice[j]).group()).replace(',',''))
    if Price[j].find('Lac') != -1:
        Final_Dict[j]['Sale_Price_Std'] = round(float((re.search(r'\d+.\d+|\d+', Price[j]).group()))*100000,2)
    elif Price[j].find('Cr') != -1:
        Final_Dict[j]['Sale_Price_Std'] = round(float((re.search(r'\d+.\d+|\d+', Price[j]).group()))*10000000,2)
    j = j + 1
print (Final_Dict)
#posts = driver.find_elements_by_class_name("tBlock")
#for post in posts:
#    print(post.text)
#print ('Start of Beautiful Soup')
#driver.find_elements_by_class_name("tBlock")
#soup = bs.BeautifulSoup(driver.page_source, "lxml")
#print(soup)
#for div in soup.find_all('div', class_='SRPriceB'):
#    print(div.text)

print (retry)
print ('Json format\n')

#json_post = json.loads(driver.find_elements_by_class_name("tBlock"))
#print(json_post)
#for post in posts:
#    print(post.text)

for i in Final_Dict:
    print(json.dumps(Final_Dict[i], indent=4))


#print(json.dumps((Final_Dict[1]), indent=4))

    

                            

                            



