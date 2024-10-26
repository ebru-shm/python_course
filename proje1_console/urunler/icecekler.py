
def icecekmenu():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║      İÇECEKLER      ║")
    print("║                     ║")
    print("║  1-Su               ║")
    print("║  2-Soda             ║")
    print("║  3-Ayran            ║")
    print("║  4-Limonata         ║")
    print("║  5-Gazoz            ║")
    print("║  6-Meyve Suyu       ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Sepete eklemek istediğiniz ürünü seçiniz: ")

    print(secim,"seçtiniz.")

    if secim == "1":
        print("Su")
    elif secim =="2":
        print("Soda")
    elif secim =="3":
        print("Ayran")
    elif secim =="4":
        print("Limonata")
    elif secim =="5":
        print("Gazoz")
    elif secim =="6":
        print("Meyve Suyu")
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")