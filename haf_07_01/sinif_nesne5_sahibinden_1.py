
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
    def __init__(self,fiyati ="Ücretsiz sahiplendirme",no ="0",adres="---",tarih="",tip="-",kimden="sahibinden"):
        super().__init__(fiyati,no,adres,tarih)
        self.EmlakTipi = tip
        self.KimdenDurumu = kimden

emlak1= Emlak("2500000","8875","Çan/Denizli","2024-11-15","Ev","Uygun")
print("Emlak tipi:", emlak1.EmlakTipi)

class KiralikEv(Emlak):
     def __init__(self,fiyat ="---",no ="0",adres="---",tarih="",tip="-",kimden="emlakçıdan",depozito=0):
            super().__init__(fiyat,no,adres,tarih,tip,kimden)
            self.Depozitos = depozito

class SatilikEv(Emlak):
    def __init__(self,fiyat ="---",no ="0",adres="---",tarih="",tip="-",kimden="emlakçıdan",tapu="Sorunsuz"):
            super().__init__(fiyat,no,adres,tarih,tip,kimden)
            self.tapuDurumu = tapu

ilan4 = SatilikEv()

print(ilan4.tapuDurumu)

ilan5 = SatilikEv(tapu ="iskansız",fiyat ="1000000")

print("ilan4.tapuDurumu:",ilan5.tapuDurumu,"\nFiyat:",ilan5.fiyat)

