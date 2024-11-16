
class Ilan():    
    fiyat = "tanimsiz"
    ilanNo= "yok"
    adres = "---"
    ilanTarihi = "tanımlanmamış"

    def __init__(ilan,fiyati=fiyat,no=ilanNo,adresi=adres,tarih=ilanTarihi):  # ilan self
        ilan.fiyat = fiyati
        ilan.ilanNo = no
        ilan.adres = adresi
        ilan.ilanTarihi = tarih


ilan1 = Ilan("Ücretsiz sahiplendirme","452","Çankaya/Ankara","2024-11-10")

# print(ilan1)
print(f"Fiyat:\t \t{ilan1.fiyat}\nAdres:\t \t{ilan1.adres}\n\
İlan no: \t{ilan1.ilanNo}\nİlan Tarihi: \t{ilan1.ilanTarihi}")


class HayvanAlemi(Ilan):     # Ilan () İlan sınıfından miras alma oluyor.
    
    # fiyat = "tanimsiz"          # miras alma sayesinde bu 4 satırı tekrar yazmadık. Bunları Ilan clasından miras aldık.
    # ilanNo= "yok"
    # adres = "---"
    # ilanTarihi = "tanımlanmamış"

    Turu = ""
    Irki = ""
    Yasi = ""
    Cinsiyeti = ""

    def __init__(xx,fiyati ="Ücretsiz sahiplendirme",no ="0",adresi="---",tarih="",tur="",irk="",yas=0,cins="Tanimsiz"):
        super().__init__(fiyati,no,adresi,tarih)
        xx.Turu = tur
        xx.Irki = irk
        xx.Yasi = yas
        xx.Cinsiyeti = cins

     
hayvan1 = HayvanAlemi("Sahiplendirme","8887","Merkez/KONYA","2024-11-11","Siyam","Kırma",2,"Erkek")
print(hayvan1.fiyat)
print(hayvan1.Yasi)

print("Hayvan1.ilanNo:", hayvan1.ilanNo)
print("Hayvan1.Yaşı:", hayvan1.Yasi)

hayvan2 = HayvanAlemi()