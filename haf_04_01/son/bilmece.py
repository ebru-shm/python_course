sorular = [
    "Su yutmuş toprağa ne denir?",
    "Ağır suya ne denir?",
    "Ateş değil ama yanar, kanatları yok ama uçar, ayakları yok ama koşar.",
    "",
]

cevaplar = [
    "Çamur",
    "Buz",
    "Güneş",
    "",
]

def menu():
    print("\n"*5," *_* KOMİK BİLMECELER *_* ")
    print("     1- Bilmece sor       ")
    print("     2- Bilmece listesi   ")
    print("     3- Bilmece cevapları ")
    print("     4- Bilmece ekleme    ")
    print("     5- Bilmece silme     ")
    print("     Seciminiz?           ")

    secim = input()
    if secim == "1" : 
        import random
        # print(sorular[2])
        rasgele_secilen_soru = random.randint(0,len(sorular)-1)
        cevap = input(f"{sorular[rasgele_secilen_soru]}")

        if cevap == cevaplar[rasgele_secilen_soru] :
            print("Süpersin..")
        else:
            print(f"Bilemedin. Doğrusu {cevaplar[rasgele_secilen_soru]} idi.")
        
    if secim == "2" :
        # print(sorular)
        print("\n\n Bilmece listesi: \n ════════════════════")
        # print(*sorular, sep="\n")
        sira = 1
        for xx in sorular:
            print (sira, "-", xx)
            sira +=1 
        
        menu()

    if secim == "3":
        print("\n\n Bilmece listesi: \n ════════════════════")
        sira = 1
        for xx in sorular:
            print (sira, "-", xx, " | Cevabı:", cevaplar[sira-1])
            sira +=1
        
        menu() 
    
    if secim == "4":
        print("\n\n Bilmece ekleme: \n ════════════════════")
        soru = input("Yeni soru giriniz:")
        cevap = input("Sorunun cevabı nedir?")
        sorular.append(soru)
        cevaplar.append(cevap)
        
        print("\n\n Eklenmiş şekli: \n ════════════════════")
        sira = 1
        for xx in sorular:
            print (sira, "-", xx, " | Cevabı:", cevaplar[sira-1])
            sira +=1
    
    
    if secim == "5":
        print("\n\n Bilmece Silme: \n ════════════════════")
        print("\n\n Mevcut bilmeceler: \n ════════════════════")
        sira = 1
        for xx in sorular:
            print (sira, "-", xx, " | Cevabı:", cevaplar[sira-1])
            sira +=1
        
        silinecek = int(input("Kaçıncı silinsin?"))
        sorular.pop(silinecek-1)
        cevaplar.pop(silinecek-1)
        
        print("\n\n Son bilmece listesi: \n ════════════════════")
        sira = 1
        for xx in sorular:
            print (sira, "-", xx, " | Cevabı:", cevaplar[sira-1])
            sira +=1
        

        
        
        
        menu() 


menu()