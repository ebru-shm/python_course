
import re
xxx = "Ahmet al renkli bir şal aldı. "

# tüm al ifadelerinin listesi
arananListe = re.findall("al",xxx)
print(f"al ifadesi Listesi: ", len(arananListe), arananListe)

# şal ifadesini ara
print("şal ifadesi var mı:", re.search("şal",xxx))

# "al" a göre bul.
print(re.split("al",xxx))

# boşlukları zzz yap.
print(re.sub(" ","zzz",xxx))