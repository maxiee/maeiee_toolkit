#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListView, QListWidget, QListWidgetItem

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle('listview')

listview = QListView()
listwidget = QListWidget()

for i in range(10):
    item = QListWidgetItem(f'Item {i}')
    listwidget.addItem(item)


def on_item_clicked(index):
    print("Item clicked", index.row())


listview.clicked.connect(lambda index: on_item_clicked(index))

listview.setModel(listwidget.model())

window.setCentralWidget(listview)
window.show()
sys.exit(app.exec_())
