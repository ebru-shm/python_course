
def sebzemenu():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║    LİSTE İŞLEMLERİ  ║")
    print("║                     ║")
    print("║  1-İndeks           ║")
    print("║  2-Sonuna ekle      ║")
    print("║  3-Son elemanı sil  ║")
    print("║  4-Uzunluk          ║")
    print("║  5-Araya ekle       ║")
    print("║                     ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    metin = input("Bir cümle yazınız: ")

    liste = list(metin)

    secim = input ("Yapmak istediğiniz işlemi giriniz: ")

    if secim == "1":
        print(liste[0])
    elif secim =="2":
        print("Biber")
    elif secim =="3":
        print("Ispanak")
    elif secim =="4":
        print("Patates")
    elif secim =="5":
        print("Domates")
    elif secim =="6":
        print("Soğan")
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")
