from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import bs4 as bs


# import urllib.request
# from urllib.parse import urlsplit, urlunsplit

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')  # Last I checked this was necessary.
options.add_argument("headless")
# set the window size
#options.add_argument('window-size=0x0')

driver = webdriver.Chrome(executable_path='C:\\Users\\morga\\Desktop\\Price Stalker\\drivers\\chromedriver.exe', options=options) 
#driver = webdriver.PhantomJS(executable_path='C:\\Users\\morga\\Desktop\\Price Stalker\\drivers\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe') 

url = 'https://www.amazon.com.au/Micro-Flex-Kick-Scooters-200m/dp/B005PZMB8Y/ref=sr_1_1?ie=UTF8&qid=1539510984&sr=8-1&keywords=micro+flex+scooter'

driver.get(url)
time.sleep(10)
html = driver.execute_script("return document.documentElement.outerHTML")

soup = bs.BeautifulSoup(html, 'html.parser')

for span in soup.find_all('span',{"id":"priceblock_ourprice"}):
    print(span.text.strip().strip('$'))
    for span in div.find_all('span',{"id":"now-price"}):
        print(span['content'])


# for div in soup.find_all('div',{"class":"price-box","itemprop":"offers" }):
#     for span in div.find_all('span',{"id":"now-price"}):
#         print(span['content'])
   

