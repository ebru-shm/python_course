
def liste_islem():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║    LİSTE İŞLEMLERİ  ║")
    print("║                     ║")
    print("║  1-Son elemanı bul  ║")
    print("║  2-Sonuna ekle      ║")
    print("║  3-Son elemanı sil  ║")
    print("║  4-Tersine çevir    ║")
    print("║  5-Araya ekle       ║")
    print("║                     ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    metin = input("Bir ifade yazınız: ")

    liste = list(metin)
    print("Liste:", liste)

    secim = input ("Yapmak istediğiniz işlemi giriniz: ")

    if secim == "1":
        print("Listenin son elemanı: ",liste[-1])
    elif secim =="2":
        yeni = input("Liste sonuna eklemek istediğiniz ifadeyi giriniz: ")
        liste.append(yeni)
        print("Yeni liste:" , liste)
    elif secim =="3":
        liste.pop()
        print("Listenin son elemanını silme işlemini seçtiniz. ")
        print("Son Liste: ", liste)
    elif secim =="4":
        print("Listeyi tersine çevir işlemini seçtiniz. ")
        print("Yeni liste:" , liste[::-1])
    elif secim =="5":
        print("Araya eleman ekleme işlemini seçtiniz. ")
        metin = input("Araya ne eklemek istiyorsunuz? ")
        indeks = int(input("Hangi indeksten önce eklemek istiyorsunuz? "))
        liste.insert(indeks,metin)
        print("Yeni liste: ",liste)
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")
