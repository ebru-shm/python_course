
import sns
from PyQt6.QtWidgets import *

class GirisEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
   
        def xxx(self):
            print("Giriş düğmesine tıklandı.")
        
        def yyy(self):
            print("Vazgeç düğmesine tıklandı.")
        


        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Adı Soyadı"))
        dikeyicerik3.addWidget(QLabel("Telefon Numarası"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())

        yi5 = QHBoxLayout()
        dugme1 = QPushButton("Giriş yap")
        yi5.addWidget(dugme1)
        dugme1.clicked.connect(xxx)      # fonksiyon parametresi olmasın.
        dugme2 = QPushButton("Vazgeç")
        yi5.addWidget(dugme2)
        dugme2.clicked.connect(yyy)


        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)

        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)

        

# class AnaEkran(QMainWindow):
#     def __init__(self):
#         super().__init__()
   
#         mainicerik = QVBoxLayout()
#         mainicerik.addWidget(QLabel("REHBER ANA EKRANI"))
#         mainicerik.addWidget(QLineEdit())
#         mainicerik.addWidget(QPushButton("Rehbere ekle"))
        
        

#         dikeyicerik3 = QVBoxLayout()
#         dikeyicerik3.addWidget(QLabel("Adı"))
#         dikeyicerik3.addWidget(QLabel("Soyadı"))

#         dikeyicerik4 = QVBoxLayout()
#         m
#         dikeyicerik4.addWidget(QLineEdit())

#         baslikBolumu = QVBoxLayout()
#         baslikBolumu.addWidget(QLabel("UYGULAMA ANA EKRANI"))

#         yi5 = QHBoxLayout()
        
#         yi5.addWidget(QPushButton("Vazgeç"))

       
#         yatayicerik.addLayout(dikeyicerik3)
#         yatayicerik.addLayout(dikeyicerik4)
#         # yatayicerik.addLayout(yi5)

#         di6.addLayout(baslikBolumu)
#         di6.addLayout(yatayicerik)
#         di6.addLayout(yi5)


#         pencere = QWidget()
#         pencere.setLayout(di6)
#         self.setCentralWidget(pencere)

class AnaEkran(QMainWindow):
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

        baslikBolumu = QVBoxLayout()
        baslikBolumu.addWidget(QLabel("UYGULAMA ANA EKRANI"))

        yi5 = QHBoxLayout()
        yi5.addWidget(QPushButton("Giriş yap"))
        yi5.addWidget(QPushButton("Vazgeç"))

       
        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(baslikBolumu)
        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)


        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)

aa = QApplication([])
pencere = GirisEkrani()
pencere.show()

ana = AnaEkran()
ana.show()
aa.exec()
