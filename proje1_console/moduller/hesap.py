
def hesaplama():
    
    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔════════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║       HESAPLAMALAR     ║")
    print("║                        ║")
    print("║  1-Toplama             ║")
    print("║  2-Çıkarma             ║")
    print("║  3-Çarpma              ║")
    print("║  4-Bölme               ║")
    print("║  5-Üs alma             ║")
    print("║                        ║")
    print("║                        ║")
    print("║    Seçimiz nedir?      ║")
    print("╚════════════════════════╝")

    sayi1 = int(input("1.sayiyi giriniz: "))
    sayi2 = int(input("2.sayiyi giriniz: "))

    secim = input("Yapmak istediğiniz işlemi seçiniz: ")           

    if secim == "1":
        print("Seçilen İşlem: Toplama")
        print(f"Sonuç: {sayi1 + sayi2}")
    elif secim =="2":
        print("Seçilen İşlem: Çıkarma")
        print(f"Sonuç: {sayi1 - sayi2}")
    elif secim =="3":
        print(f"Sonuç: {sayi1*sayi2}")
    elif secim =="4":
        print("Seçilen İşlem: Bölme")
        print(f"Sonuç: {sayi1/sayi2}")
    elif secim =="5":
        print("Seçilen İşlem: Üs alma")
        print(f"Sonuç: {sayi1**sayi2}")
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")