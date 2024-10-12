
sayi = int(input("Sayı:"))

if sayi > 100:  print("Sayı 100'den büyüktür.")
elif sayi <= 100:  print("Sayı 100'den küçük değildir.")


print("Chat GPTV'ye hoş geldin.")

cevap = input("Nasılsın: ")
# if cevap == "iyiyim" or cevap == "iyi" or cevap =="güzel":
if cevap in ["iyiyim","iyi","güzel"]:  # bu ile üst satır aynı işi yapar.
    print("Güzel, iyi olmana sevindim.")

if cevap in ["kötü","moralim bozuk"]:
    c= print("Hayırdır ne oldu?")
    if c in ["sınavım kötü geçti","sınav kötüydü","istediğim motor satılmış"]:
        print("Böyle şeyleri takma.")
    if c in ["otobüsü kaçırdım","sınavım kötüydü"]:  # elif olsaydı sınav kötüydü ifadesinde sonraki satır çalışmazdı.
        print("sonraki sefere, olmaz inş.")



input()