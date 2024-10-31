
def model_oneri():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║   ÜRÜN ÖNERİLERİ    ║")
    print("║                     ║")
    print("║  1-Telefon          ║")
    print("║  2-Televizyon       ║")
    print("║  3-Tost Makinesi    ║")
    print("║  4-Bilgisayar       ║")
    print("║  5-Süpürge          ║")
    print("║                     ║")
    print("║                     ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

  
    secim = input("Yapmak istediğiniz işlemi seçiniz: ")


    if secim == "1":
        print(["Apple","oppo","Samsung","Huawei"])
    elif secim =="2":
        print(["LG","Philips","Vestel","Samsung"])
    elif secim =="3":
        print(["Arzum","Karaca","Arçelik","Tefal","Korkmaz"])
    elif secim =="4":
        print(["HP","Asus","Lenovo","Samsung","Apple"])
    elif secim =="5":
        harf = input(["Arçelik","Dyson","Philips","Karaca"])
    else:
        print("Seçmek istediğiniz kategori mevcut değildir, lütfen tekrar seçim yapınız.")