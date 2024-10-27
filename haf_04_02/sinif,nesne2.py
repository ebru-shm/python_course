
class Ogrenci():
    adi = "-"
    ortalamasi = 50


print(Ogrenci)
print(Ogrenci.adi)
print(Ogrenci.ortalamasi)

ogrenci1 = Ogrenci()   # öğrenci1 nesne oluyor.
print(ogrenci1)
print(ogrenci1.adi)
print(ogrenci1.ortalamasi)

ogrenci1.adi = "Nurdan Sarı"
print(ogrenci1.adi)

ogrenci2 = Ogrenci()
print(ogrenci2.adi)
print(Ogrenci.adi)

ogrenci2.adi = "Ömer Aybak"
print(ogrenci2.adi)
print(ogrenci1.adi)