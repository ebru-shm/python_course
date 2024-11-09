
import re

metin1 = "Bugün hava çok soğuk"
metin2 = "Burası çok sıcak"
metin3 = "Bugün hava çok soğuk"

# aranan = "^Bu.*soğuk$"  # başında bu olan ve sıcak ile biten
# aranan = "^Bug.*" # başında Bug olanları ara
aranan = "o.*" # o ile başlayan ifadeler


print(re.search(aranan,metin1))
print(re.search(aranan,metin2))
print(re.search(aranan,metin3))

deger = re.search(aranan, metin1)
print(type(deger))





