
class Ogrenci():    # büyük veri tipi
    ad = "tanimsiz"
    tc = "yok"
    ortalamasi = 0

print(Ogrenci.ad)

print(type(Ogrenci))
print(type(Ogrenci.ad))

ogrenci1 = Ogrenci()
print(type(ogrenci1))
print(type(ogrenci1.ad))
print(ogrenci1.ad)
ogrenci1.ad = "Muhammed Ali"
print(ogrenci1.ad)

ogrenci2 = Ogrenci()      # () koyduğumuzda initialize ediyoruz, yani yeni bir nesne tanımlanıyor.
ogrenci2.ad = "Ebru"

print("ogrenci2.ad:", ogrenci2.ad)
print("ogrenci1.ad:", ogrenci1.ad)

print(Ogrenci)
