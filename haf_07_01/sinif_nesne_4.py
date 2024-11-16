
class Ogrenci():    # büyük veri tipi ( sınıflar veri kalıbıdır)
    ad = "tanimsiz"
    tc = "yok"
    ortalamasi = 10
    def _init_(xx,aa="",bb=tc,cc= ortalamasi):  # xx ifadesi yerine genelde self ifadesi kullanılır.
        xx.ad = aa
        xx.tc = bb
        xx.ortalamasi = cc

# ogrenci1 = Ogrenci()
# ogrenci1.ad = "Sude"           # bu ve sonraki 3 satır ile yeni nesne özellikleri ayarlanır.
# ogrenci1.tc = "522334444665"
# ogrenci1.ortalamasi = 99


ogrenci1 = Ogrenci("Sude","522334444665",98)           # bu satır üstteki 3 satırın yaptığı işi yapar.
ogrenci1.disiplinNotu = 100
print("ogrenci1.disiplinNotu", ogrenci1.disiplinNotu)


ogrenci2 = Ogrenci()
ogrenci2.ad = "Rahime"
ogrenci2.tc = "41567834566"

print("Ogrenci Ortalamasi: ",ogrenci2.ortalamasi)
print("Ogrenci Adi: ",ogrenci2.ad)

ogrenci3 = Ogrenci ()                # init'i çalıştırır.
print("Ogrenci adi: ", ogrenci3.ad)

ogrenci4 = Ogrenci                  # init fonksiyunu çalıştırılmadan nesne oluşur. (tercih edilen bir durum değildir.)
print("Ogrenci adi: ", ogrenci4.ad)

