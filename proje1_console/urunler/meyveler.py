
def meyvemenu():
      
    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║         MEYVE       ║")
    print("║                     ║")
    print("║  1-Elma             ║")
    print("║  2-Armut            ║")
    print("║  3-Çilek            ║")
    print("║  4-Mandalina        ║")
    print("║  5-Üzüm             ║")
    print("║  6-Ayva             ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Sepete eklemek istediğiniz ürünü seçiniz: ")

    print(secim,"seçtiniz.")

    if secim == "1":
        print("Elma")
    elif secim =="2":
        print("Armut")
    elif secim =="3":
        print("Çilek")
    elif secim =="4":
        print("Mandalina")
    elif secim =="5":
        print("Üzüm")
    elif secim =="6":
        print("Ayva")
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")
