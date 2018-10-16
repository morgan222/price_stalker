
import integration as intg
import sel_scrape as sel_scrape
import bs4 as bs
import urllib.request
from urllib.parse import urlsplit, urlunsplit


#using python 3.7
def run_test(path):

    df_data = intg.read_csv(path)
    
    driver = sel_scrape.initialise_driver()
    #get price
    for i, row in df_data.iterrows():
        email = row['email']
        url = row['url']
        price_fileter = row['price_filter']

        price = None
        availability = None

        #need to mimic a browser - using pyqt4 -- pnly really need this for javascript

        split_url = urlsplit(url)
        base_url = split_url.scheme + '://' + split_url.netloc
        
        #returns a soup
        soup = sel_scrape.get_url(driver, url)

        if base_url == 'https://www.microscooters.com.au':
          #Scrape price for promotion first
          for div in soup.find_all('div',{"class":"price-box","itemprop":"offers" }):
              for span in div.find_all('span',{"id":"now-price"}):
                  price = float(span['content'].strip())

          #Get price if not promoted
          if price is None:
            for div in soup.find_all('div',{"class":"price-box","itemprop":"offers" }):
                for span in div.find_all('span',{"class":"price"}):
                    price = float(span['content'].strip())


        if base_url == 'https://www.georgesbikeshop.com.au':
          #for non promotions and promotions:
          for div in soup.find_all('div',{"itemprop":"offers"}):
              for meta in div.find_all('meta',{"itemprop":"price"}):
                  price = float(meta['content'].strip())

        if base_url == 'https://www.skaterhq.com.au':
          #for promotions
          for div in soup.find_all('div',{"class":"product-type-data"}):
              for p in div.find_all('p',{"class":"special-price"}):
                  for span in p.find_all('span',{"class":"price"}):
                      price = float(span.text.strip().strip('$'))
                     
          #non promotions
          if price is None:
              #for non promotions
              for div in soup.find_all('div',{"class":"product-type-data"}):
                  for span in div.find_all('span',{"class":"price"}):
                      price = float(span.text.strip().strip('$'))

        if base_url == 'https://www.amazon.com.au':
            for span in soup.find_all('span',{"id":"priceblock_ourprice"}):
                price = float(span.text.strip().strip('$'))

        print(base_url, price)


if __name__ == '__main__':
    run_test('C:\\Users\\morga\\Desktop\\Price Stalker\\data.csv')