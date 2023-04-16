import sys
from PyQt5.QtCore import *
# command :pip install PyQt5
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtWidgets import *
# command :pip install PyQtWebEngine
from PyQt5.QtWebEngineWidgets import*
class WebClass(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        self.showMaximized()
        self.browser=QWebEngineView()
        self.setCentralWidget(self.browser)
        self.browser.setUrl(QUrl('https://google.com'))
        #------------------menu------------
        self.menu=QToolBar()
        self.addToolBar(self.menu)

        back_button=QAction('Back',self)
        back_button.triggered.connect(self.browser.back)
        self.menu.addAction(back_button)

        next_button=QAction('Next',self)
        next_button.triggered.connect(self.browser.forward)
        self.menu.addAction(next_button)

        reload_button=QAction('Refresh',self)
        reload_button.triggered.connect(self.browser.reload)
        self.menu.addAction(reload_button)

        home_button=QAction('Home',self)
        home_button.triggered.connect(self.Home_Url)
        self.menu.addAction(home_button)

        self.url_txt=QLineEdit()
        self.url_txt.returnPressed.connect(self.Navigate_Url)
        self.menu.addWidget(self.url_txt)

        self.browser.urlChanged.connect(self.Update_Url)

    # _______________ #Functions _____________________________  
    def Home_Url(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def Navigate_Url(self):
        self.browser.setUrl(QUrl(self.url_txt.text())) 

    def Update_Url(self,URL):
        self.url_txt.setText(URL.toString())


WebApp=QApplication(sys.argv)
QApplication.setApplicationName("Browser - Developed By Riket")
obj=WebClass()
WebApp.exec_()