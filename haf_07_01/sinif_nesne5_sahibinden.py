
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

print(ilan1)
print(f"Fiyat:\t \t{ilan1.fiyat}\nAdres:\t \t{ilan1.adres}\n\
İlan no: \t{ilan1.ilanNo}\nİlan Tarihi: \t{ilan1.ilanTarihi}")