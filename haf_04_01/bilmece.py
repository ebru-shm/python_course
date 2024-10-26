

sorular = [
    "Su yutmuş toprağa ne nedir?",
    "Ağır suya ne denir?",
    "Ateş değil ama yanar, kanatları yok ama uçar, ayakları yok ama koşar.",
    "",
]

cevaplar = [
    "Çamur",
    "Buz",
    "Güneş"
    "",
]


def menu():
    print("\n"*5, "*_* KOMİK BİLMECELER *_* ")
    print("   1- Bilmece Sor          ")
    print("   2- Bilmece Listesi      ")
    print("   3- Bilmece Cevapları    ")
    print("   4- Bilmece Ekleme       ")
    print("   5- Bilmece Silme        ")
    print("   Seçiminiz?              ")

    secim = input()
    if secim == "1":
        import random
        # print(sorular[2])
        rastgelesecilensoru = random.randint(0,len(sorular))
        cevap = input(f"{sorular[rastgelesecilensoru]}")

        if cevap.lower() == cevaplar[rastgelesecilensoru]:
            print("süpersin..")
        else:
            print(f"Bilemedin, doğrusu {cevaplar[rastgelesecilensoru]} idi.")

     
    if secim == "2":
        # print(sorular)
        print("\n\n Bilmece Listesi: \n ----------------")
        # print(*sorular, sep = "\n")
        sira = 1
        for soru in sorular:
            print(sira,"-", soru)
            sira +=1
        menu()
    if secim == "3":
        print("\n\n Bilmece Listesi: \n ----------------")
        # print(*sorular, sep = "\n")
        sira = 1
        for cevap in cevaplar:
            print(sira,"-", cevap," / Cevabı", cevaplar[sira-1])
            sira +=1
        menu()
    if secim == "4":
        print("\n\n Bilmece Ekleme: \n ----------------")
        soru = input("Yeni soru giriniz: ")
        cevap = input ("Sorunun cevabı nedir? ")
        sorular.append(soru)
        cevaplar.append(cevap)
        
        print("\n\n Eklenmiş hali: \n ----------------")
        sira = 1
        for xx in sorular:
            print(sira,"-", xx," / Cevabı", cevaplar[sira-1])
            sira +=1
            
        menu()
     if secim == "5":
            print("\n\n Bilmece Silme: \n ----------------")
            print("\n\n Mevcut Bilmeceler: \n ----------------")
        sira = 1
        for xx in cevaplar:
            print(sira,"-", xx," / Cevabı", cevaplar[sira-1])
            sira +=1
    silinecek = int(input("Kaçıncı silinsin: "))
    
        cevap = input ("Sorunun cevabı nedir? ")
        sorular.append(soru)
        cevaplar.append(cevap)
        print("\n\n Eklenmiş hali: \n ----------------")
        sira = 1
        
        menu()

menu()