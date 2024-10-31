
def stringislem():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║   STRING İŞLEMLERİ  ║")
    print("║                     ║")
    print("║  1-Upper            ║")
    print("║  2-Lower            ║")
    print("║  3-Replace          ║")
    print("║  4-Find             ║")
    print("║  5-Count            ║")
    print("║                     ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    metin = input ("Metinsel bir ifade giriniz: ")
    print(f"Girilen ifade '{metin}'")
    
    secim = input("Yapmak istediğiniz işlemi seçiniz: ")


    if secim == "1":
        print(metin.upper())
    elif secim =="2":
        print(metin.lower())
    elif secim =="3":
        eski = input ("Değiştirmek istediğiniz ifade: ")
        yeni = input ("Yeni: ")
        print("Yeni metin:",metin.replace(eski, yeni))
    elif secim =="4":
        bul = input ("Metin içinde aradığınız ifade: ")
        print(metin.find(bul))
    elif secim =="5":
        harf = input("Bir harf giriniz: ")
        print(metin.count(harf))
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")