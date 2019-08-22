import requests
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QTableWidgetItem, QMainWindow, QWidget, QGridLayout, QApplication, QTableWidget
from bs4 import BeautifulSoup


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(1200, 800))
        self.setWindowTitle("Warthander")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        table = QTableWidget(self)
        table.setColumnCount(4)
        table.setRowCount(1)

        table.setHorizontalHeaderLabels(["Заголовок", "Время", "Комментарии", "Текст"])

        page = requests.get('https://warthunder.ru/ru/')
        soup = BeautifulSoup(page.text, 'html.parser')
        articles = soup.find_all('div', class_='news-item')

        for i in range(len(articles)-1):
            article = articles[i]

            main = article.find(class_="news-item__title")
            time = article.find(class_="news-item__additional-date")
            text = article.find(class_="news-item__text")
            comments = article.find('a', class_="news-item__additional-comment")
            if comments is not None:
                print(comments.get_text())

            table.setRowCount(i + 1)

            table.setItem(i, 0, QTableWidgetItem(main.get_text()))
            table.setItem(i, 1, QTableWidgetItem(time.get_text()))
            table.setItem(i, 3, QTableWidgetItem(text.get_text()))
            if comments is not None:
                table.setItem(i, 2, QTableWidgetItem(comments.get_text()))

        table.resizeColumnsToContents()
        grid_layout.addWidget(table, 0, 0)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
