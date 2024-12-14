from PyQt6.QtWidgets import *

class GirisEkrani(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Program Giriş Ekranı')
        # self.resize(300,50)
        self.setFixedSize(300,100)

        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Kullanıcı adı"))
        dikeyicerik3.addWidget(QLabel("Şifresi"))

        dikeyicerik4 = QVBoxLayout()
        self.kullanici_adi = QLineEdit()
        dikeyicerik4.addWidget(self.kullanici_adi)

        self.sifre = QLineEdit()
        dikeyicerik4.addWidget(self.sifre)
       
        yi5 = QHBoxLayout()
        dugme1 = QPushButton("Giriş yap")
        yi5.addWidget(dugme1)
        # dugme1.clicked.connect(self.xxx) # fonksiyon parantezi olmasın
        dugme1.clicked.connect(self.kontrol) # fonksiyon parantezi olmasın
        
        dugme2 = QPushButton("Vazgeç")
        yi5.addWidget(dugme2)
        dugme2.clicked.connect(self.vazgec)

        yatayicerik.addLayout(dikeyicerik3)
        yatayicerik.addLayout(dikeyicerik4)
        # yatayicerik.addLayout(yi5)

        di6.addLayout(yatayicerik)
        di6.addLayout(yi5)

        pencere = QWidget()
        pencere.setLayout(di6)
        self.setCentralWidget(pencere)

    def xxx(self,x):
        mesaj = "Giriş düğmesine tıklandı."
        print(mesaj)
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Dikkat")
        dlg.setText(mesaj)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.exec()
        # sonuc = dlg.exec()
        # if sonuc == QMessageBox.Yes:
        #     print("Yes!")
        # else:
        #     print("No!")
        
    def kontrol(self):
        dka = "q"
        dsf = "q"

        # dosya = open("bilgiler.txt")
        # dka = dosya.readline()
        # dsf = dosya.readline()

        print("Doğru kullanıcı adı: ", dka)
        print("Doğru şifre: ", dsf)
        ka = self.kullanici_adi.text()
        sf = self.sifre.text()
        print(f"Giriş düğmesine tıklandı.\nGirilen kullanıcı adı:{ka}\nGirilen şifre:{sf}")
        if dka == ka and dsf == sf :
            print("Yetki var, ana ekrana yönlendiriliyorsunuz.")
            self.ana = AnaEkran()
            self.ana.show()
            self.close()
        else:
            print("Kullanım yetkisi yok.")

    def vazgec(self):
        print("vazgeç düğmesine tıklandı.")
        aaa = QMessageBox(self)
        aaa.setWindowTitle("Aman Dikkat")
        aaa.setText("Vazgeç düğmesine tıkladınız.")
        aaa.exec()

class AnaEkran(QMainWindow):
    def __init__(self):
        super().__init__()
   
        mainIcerik = QVBoxLayout()
        
        mainIcerik.addWidget(QLabel("REHBER ANA EKRANI"))
        buton1 = QPushButton("Rehbere ekle")
        buton1.clicked.connect(self.ekle)

        mainIcerik.addWidget(buton1)
        buton2 = QPushButton("Listele")
        mainIcerik.addWidget(buton2)
        buton2.clicked.connect(self.listele)
        mainIcerik.addWidget(QPushButton("Düzelt"))
        mainIcerik.addWidget(QPushButton("..."))
        self.labelListe = QLabel("Liste burada görünecek")
        mainIcerik.addWidget(self.labelListe)

        pencere = QWidget()
        pencere.setLayout(mainIcerik)
        self.setCentralWidget(pencere)
    def ekle(self):
        self.ekle = EklemeEkrani()
        self.ekle.show()

    def listele(self):
        print("Listele düğmesine basıldı")
        import mysql.connector
        try:
        
            vts = mysql.connector.connect(host="localhost",user="root",password="1234",
            database="deneme1"
            ); print("Bağlantı tamam:")  
            secilen = vts.cursor()
            alinan_liste = secilen.execute("select * from ogrenciler")
            # xxx = secilen.fetchone() # fetchone ile sadece bir kayıt alınır
            xxx = secilen.fetchall() # fetchall ile tüm kayıtlar alınır
            # print(xxx)
            self.labelListe.setText("")
            for a in xxx:
                print(a)               
                self.labelListe.setText(f"{self.labelListe.text()}\n{a[0]},{a[4]}")
        
        except: # veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
            print("Veritabanına bağlanırken bir hata oluştu.")


class EklemeEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
   
        di6 = QVBoxLayout()
        yatayicerik = QHBoxLayout()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Adı soyadı:"))
        dikeyicerik3.addWidget(QLabel("Telefon numarası:"))

        dikeyicerik4 = QVBoxLayout()
        self.ad = QLineEdit()
        dikeyicerik4.addWidget(self.ad)
        self.numara = QLineEdit()
        dikeyicerik4.addWidget(self.numara)
       
        baslikBolumu = QHBoxLayout()
        baslikBolumu.addWidget(QLabel("YENİ KAYIT EKLEME EKRANI"))
        
        yi5 = QHBoxLayout()
        butonKaydet = QPushButton("Kaydet")
        yi5.addWidget(butonKaydet)
        butonKaydet.clicked.connect(self.kaydet)

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
    def kaydet(self):
        print("Kaydet fonksiyonu çalıştı.")
        import mysql.connector
        try:
            vts = mysql.connector.connect(host="localhost",user="root",password="1234",
            database="deneme1"
            ); print("Bağlantı tamam:")  

            try:
                secilen = vts.cursor()
                # secilen.execute("CREATE TABLE ogrenciler (ad VARCHAR(50), telefon VARCHAR(30))")
                adi = self.ad.text()
                num = self.numara.text()
                secilen.execute(f"INSERT INTO ogrenciler (ad, telefon) VALUES ('{adi}', '{num}')")
                vts.commit()

                print("kayıt eklendi.")
            except mysql.connector.Error as hata:
                print(f"Hata : {hata}")  

        except: # veritabanı sistemine bağlanma sistem kurulu değilse veya herhangi bir eksik varsa hata verecektir.
            print("Veritabanına bağlanırken bir hata oluştu.")


aa = QApplication([])
pencere = GirisEkrani()
pencere.show()

# ana = AnaEkran()
# ana.show()
aa.exec()