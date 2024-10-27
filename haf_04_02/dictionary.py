
ogrenciler = ["Sude AKYOL","Rahime KARA"]
ortalamalar = [79,89]

# ogrenciOrtalamalari = {
#                 "adi1" : "Sude AKYOL", "ortalamasi1": 80,
#                 "adi2" : "Rahime KARA", "ortalamasi2": 90}

# print(ogrenciOrtalamalari)
# print(ogrenciOrtalamalari["adi1"], ogrenciOrtalamalari["ortalamasi1"])

ogrenciOrtalamalari = {
                "ogrenci1" :{"adi" : "Sude AKYOL", "ortalamasi": 80},
                "ogrenci2" :{"adi" : "Rahime KARA", "ortalamasi": 90},
                }

print(ogrenciOrtalamalari["ogrenci1"]["adi"])


ogrenciOrtalamalari = {
                "123456" :{"adi" : "Sude AKYOL", "ortalamasi": 80},
                "345678" :{"adi" : "Rahime KARA", "ortalamasi": 90},
                }

print(ogrenciOrtalamalari["345678"]["adi"])

aranacak = input("Hangi öğrenci bilgileri: ").strip()
if aranacak != "":
    print(ogrenciOrtalamalari[aranacak]["adi"])
else: print("boş geçme")
