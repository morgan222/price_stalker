import sys
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4.QtCore import *
# app = QApplication(sys.argv)
# #QWebPage.loadFinished.connect()
# button = QPushButton("Hello World", None)
# button.show()
# app.exec_()
# from PyQt5.QtWidgets  import QApplication
# from PyQt5.QtWebEngineWidgets import QWebEngineView
# from PyQt4.QtCore import QUrl
# from PyQt4.QtWebKit import QWebPage
import bs4 as bs
import urllib.request

class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()
        
    def on_page_load(self):
        self.app.quit()
     
url = 'https://www.officeworks.com.au/shop/officeworks/p/kindle-touch-2016-6-ereader-black-amkindt6b?cm_mmc=Google:SEM:Shopping:Ereaders:AMKINDT6B&cm_mmca1=NULL&cm_mmca3=conversion&cm_mmca9=columbus&CAWELAID=620015440002473839&CAGPSPN=pla&CAAGID=34435309398&CATCI=pla-295800965906&gclid=EAIaIQobChMIiaiurI-F3gIVA6qWCh1rWQl-EAQYAiABEgJhe_D_BwE&gclsrc=aw.ds,120'
client_response = Client(url)
source = client_response.mainFrame().toHtml()
soup = bs.BeautifulSoup(source, 'lxml')





#js_test = soup.find('p', class_='jstest')
#print(js_test.text)