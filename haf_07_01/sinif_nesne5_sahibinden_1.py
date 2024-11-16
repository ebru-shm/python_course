
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

class Emlak(Ilan):
    def __init__(self,fiyati ="Ücretsiz sahiplendirme",no ="0",adres="---",tarih="",tip="-",kredi="olur"):
        super().__init__(fiyati,no,adres,tarih)
        self.EmlakTipi = tip
        self.KrediDurumu = kredi

emlak1= Emlak("2500000","8875","Çan/Denizli","2024-11-15","Ev","Uygun")
print("Emlak tipi:", emlak1.EmlakTipi)

class KiralikEv(Emlak):
    pass

class SatilikEv(Emlak):
    pass

