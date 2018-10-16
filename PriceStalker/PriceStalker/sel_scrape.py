from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import bs4 as bs


def initialise_driver():

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

    return driver

#takes the driver and url, and returns the soup
def get_url(driver, url):

    driver.get(url)
    time.sleep(10)
    html = driver.execute_script("return document.documentElement.outerHTML")

    soup = bs.BeautifulSoup(html, 'html.parser')

    return soup




# for div in soup.find_all('div',{"class":"ow-product-details__top"}):
#     for span in div.find_all('span',{"class":"price-ele"}):
#         print(span)


# for div in soup.find_all('div',{"class":"ow-product-details__top"}):
#     for span in div.find_all('span',{"class":"price-ele"}):
#         print(span)

