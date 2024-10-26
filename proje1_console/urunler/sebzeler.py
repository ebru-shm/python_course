
def sebzemenu():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║        SEBZE        ║")
    print("║                     ║")
    print("║  1-Salatalık        ║")
    print("║  2-Biber            ║")
    print("║  3-Ispanak          ║")
    print("║  4-Patates          ║")
    print("║  5-Domates          ║")
    print("║  6-Soğan            ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Sepete eklemek istediğiniz ürünü seçiniz: ")

    print(secim,"seçtiniz.")

    if secim == "1":
        print("Salatalık")
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
