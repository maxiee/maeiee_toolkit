#!/usr/bin/env python

import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QListWidget, QListWidgetItem, QWidget, QVBoxLayout, QLabel

data = []

if len(sys.argv) > 1:
    data = json.loads(sys.argv[1])
elif sys.stdin:
    data = json.loads(str(sys.stdin.read()))

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('listview')

listwidget = QListWidget()


class InfoCard(QWidget):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        title = QLabel(data['title'])
        description = QLabel(data['description'])
        layout.addWidget(title)
        layout.addWidget(description)
        self.setLayout(layout)


for i in range(len(data)):
    item = QListWidgetItem(listwidget)
    card = InfoCard(data[i], parent=listwidget)
    item.setSizeHint(card.sizeHint())
    listwidget.addItem(item)
    listwidget.setItemWidget(item, card)


def on_item_clicked(index):
    print("Item clicked", index.row())


listwidget.clicked.connect(lambda index: on_item_clicked(index))

window.setCentralWidget(listwidget)
window.show()
sys.exit(app.exec_())
