
import sys
# from PyQt5.QtWidgets import QApplication, QPushButton
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)

nesne = QPushButton("Tıkla")
nesne.show()

nesne1 = QLabel("Ekle")
nesne1.show()

app.exec()
