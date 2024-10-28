
def sutmenu():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║      SÜT ÜRÜNLERİ   ║")
    print("║                     ║")
    print("║  1-Beyaz Peynir     ║")
    print("║  2-Yoğurt           ║")
    print("║  3-Kaşar Peyniri    ║")
    print("║  4-Tereyağı         ║")
    print("║  5-Kaymak           ║")
    print("║  6-Krem Peyniri     ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Sepete eklemek istediğiniz ürünü seçiniz: ")

    print(secim,"seçtiniz.")

    if secim == "1":
        print("Beyaz Peynir")
    elif secim =="2":
        print("Yoğurt")
    elif secim =="3":
        print("Kaşar Peyniri")
    elif secim =="4":
        print("Tereyağı")
    elif secim =="5":
        print("Kaymak")
    elif secim =="6":
        print("Krem Peyniri")
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")
