
import re
xxx = "Ahmet al renkli bir şal aldı. "

# tüm al ifadelerinin listesi
arananListe = re.findall("al",xxx)
print(f"al ifadesi Listesi: ", len(arananListe), arananListe)

arananListe = re.findall("al/en",xxx)
print(f"al ifadesi Listesi: ", len(arananListe), arananListe)

arananListe = re.findall("al* ",xxx)
print(f"al ifadesi Listesi: ", len(arananListe), arananListe)