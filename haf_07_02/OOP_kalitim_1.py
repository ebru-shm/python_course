
class Personel():
    sicilNo = "--"
    adiSoyadi = "tanimsiz"


class Idareci(Personel):
    idariGörevi = "tanımlanmamis"

class KatPersoneli(Personel):
    gorevliOLduguKat = 4

class Veli():
    ogrencininAdi = "-----"

class CokluYetkiliPersonel(Idareci, Veli):  # çoklu miras alma. Multiple inheritance
    pass



personel1 = Idareci()
personel2 = CokluYetkiliPersonel()
personel2.idariGörevi = "Müdür yardımcısı"
personel2.ogrencininAdi = "Ufuk ALTIN"


print(personel1.sicilNo)
# print(personel1.gorevliOlduguKat)

print("İdari görev: ",personel2.idariGörevi,"\nÖğrenci adı: ", personel2.ogrencininAdi)