import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel
import requests
from bs4 import BeautifulSoup

class WebCrawlerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Web Crawler')
        self.resize(800, 600)
        self.UI()

    def UI(self):
        layout = QVBoxLayout()
        self.urlLabel = QLabel("Enter URL : ",self)
        layout.addWidget(self.urlLabel)

        self.urlLineEdit = QLineEdit(self)
        self.urlLineEdit.setPlaceholderText('https://example.com')
        layout.addWidget(self.urlLineEdit)

        self.crawlButton = QPushButton('crawl',self)
        self.crawlButton.clicked.connect(self.crawlWebsite)
        layout.addWidget(self.crawlButton)    

        self.resultsLabel = QLabel("Results :",self)
        layout.addWidget(self.resultsLabel)

        self.resultTextEdit = QTextEdit(self)
        self.resultTextEdit.setPlaceholderText('Crawled data will be shown here ...')
        layout.addWidget(self.resultTextEdit)

        self.setLayout(layout)

    def crawlWebsite(self):
        url = self.urlLineEdit.text()
        try :
            response = requests.get(url)
            soup = BeautifulSoup(response.content,'html.parser')
            #print(soup)

            links = soup.find_all('a')
            #print(links)
            result_text = ""
            for link in links :
                href = link.get('href')
                if href is not None :
                    result_text += href + "\n"

            self.resultTextEdit.setPlainText(result_text)

        except Exception as e:
            self.resultTextEdit.setPlainText(f'Error : {e}')







def main():
    app = QApplication(sys.argv)
    window = WebCrawlerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
