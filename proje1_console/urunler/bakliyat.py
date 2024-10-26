
def bakliyatmenu():
    
    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║      BAKLİYAT       ║")
    print("║                     ║")
    print("║  1-Fasulye          ║")
    print("║  2-Nohut            ║")
    print("║  3-Kırmızı Mercimek ║")
    print("║  4-Bulgur           ║")
    print("║  5-Pirinç           ║")
    print("║  6-Yeşil Mercimek   ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Sepete eklemek istediğiniz ürünü seçiniz: ")

    print(secim,"seçtiniz.")

    if secim == "1":
        print("Fasulye")
    elif secim =="2":
        print("Nohut")
    elif secim =="3":
        print("Kırmızı Mercimek")
    elif secim =="4":
        print("Bulgur")
    elif secim =="5":
        print("Pirinç")
    elif secim =="6":
        print("Yeşil Mercimek")
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")