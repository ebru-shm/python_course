
import sns
from PyQt6.QtWidgets import *

class GirisEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
   
        
        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Adı"))
        dikeyicerik3.addWidget(QLabel("Soyadı"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())

        yi5 = QHBoxLayout()
        yi5.addWidget(QPushButton("Giriş yap"))
        yi5.addWidget(QPushButton("Vazgeç"))

       
        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)


        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)

aa = QApplication([])
pencere = GirisEkrani()
pencere.show()
aa.exec()
