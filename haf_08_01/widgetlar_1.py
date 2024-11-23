

import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
pencere = QMainWindow()

tepsi_1 = QVBoxLayout()         # vertical
# layout = QHBoxLayout()        # horizontal


tepsi_1.addWidget(QLabel("Kullanıcı adı"))
tepsi_1.addWidget(QLineEdit())

tepsi_1.addWidget(QLabel("şifre: "))
tepsi_1.addWidget(QLineEdit())

tepsi_1.addWidget(QPushButton("Giriş"))
tepsi_1.addWidget(QCheckBox("Beni hatırla"))


sunum_tepsisi= QWidget()
sunum_tepsisi.setLayout(tepsi_1)

pencere.setCentralWidget(sunum_tepsisi)

pencere.show()
app.exec()









# 1 tane layoutu seçip sonra alt tuşuna basarak tüm layoutları seç, sonra hepsini tepsi_1 olarak değiştir.