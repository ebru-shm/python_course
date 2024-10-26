
def temizlikmenu():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔══════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║  TEMİZLİK ÜRÜNLERİ   ║")
    print("║                      ║")
    print("║  1-Bulaşık Deterjanı ║")
    print("║  2-Çamaşır Suyu      ║")
    print("║  3-Çamaşır Deterjanı ║")
    print("║  4-Islak Mendil      ║")
    print("║  5-Kağıt Havlu       ║")
    print("║  6-Yumuşatıcı        ║")
    print("║                      ║")
    print("║    Seçimiz nedir?    ║")
    print("╚══════════════════════╝")

    secim = input("Sepete eklemek istediğiniz ürünü seçiniz: ")

    print(secim,"seçtiniz.")

    if secim == "1":
        print("Bulaşık Deterjanı")
    elif secim =="2":
        print("Çamaşır Suyu")
    elif secim =="3":
        print("Çamaşır Deterjanı")
    elif secim =="4":
        print("Islak Mendil")
    elif secim =="5":
        print("Kağıt Havlu")
    elif secim =="6":
        print("Yumuşatıcı")
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")



    # en az 5 seçim olsun.
    # ana menude en az 5 seçenek olsun.

    # google arama butonuna gel- adres çubuğuna alt + 201 vs. yaz bırak o simge geliyor.