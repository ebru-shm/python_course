
class Ogrenci():    # Kalıp
    adi = "--"
    ortalamasi = 50
    # soyadi = ""
    def __init__(aa,xx,yy):  # aa = self = kendine ait şeyleri
        aa.adi = xx
        aa.ortalamasi = yy
    # def __init__(self,adi,ortalamasi):  # aa = self = kendine ait şeyleri
    #     self.adi = adi
    #     self.ortalamasi = ortalamasi

# ogrenci1 = Ogrenci()        # sınıftan nesne oluşturma
# ogrenci1.adi = "Buse Doğan"
# ogrenci1.ortalamasi = 80
ogrenci1 = Ogrenci("Buse AYDOĞAN",81)   # sınıftan nesne oluşturma

# ogrenci2 = Ogrenci()
# ogrenci2.adi = "Ebru Gündeş"
# ogrenci2.ortalamasi = 90
ogrenci2 = Ogrenci("Ebru Gündeş",90)   # sınıftan nesne oluşturma

print(ogrenci2)
print(ogrenci2.adi)
# print(ogrenci2.soyadi)


class Ogretmen():
    adi = "--"
    soyadi = "--"
    sorumlu_oldugu_sinif = "-"
    brans = "--"
    tc = "--"

    def __init__(bb,kk,mm,tt,ss):  # bb = self = kendine ait şeyleri
        bb.adi = kk
        bb.soyadi = mm
        bb.brans = tt
        bb.tc = ss


# ogretmen1 = Ogretmen()
# ogretmen1.adi = "Esra"
# ogretmen1.soyadi = "Aydın"
# ogretmen1.brans = "Matematik"
# ogretmen1.tc = "123456"

ogretmen1 = Ogretmen("Esra","Aydın","Matematik","123456")

print(ogretmen1.adi)
print(ogretmen1.brans)



