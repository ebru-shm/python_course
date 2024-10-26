import urunler.bakliyat
import urunler.icecekler
import urunler.meyveler
import urunler.sebzeler
import urunler.sut_urunleri
import urunler.temizlik
def urunmenu():

    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔══════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║      ÜRÜN LİSTESİ    ║")
    print("║                      ║")
    print("║  1-İçecekler         ║")
    print("║  2-Meyve             ║")
    print("║  3-Sebze             ║")
    print("║  4-Bakliyat          ║")
    print("║  5-Süt ürünleri      ║")
    print("║  6-Temizlik Ürünleri ║")
    print("║                      ║")
    print("║                      ║")
    print("║  Seçimiz nedir?      ║")
    print("╚══════════════════════╝")

    secim = input("işlem yapmak istediğiniz kategoriyi seçiniz: ")

    print(secim,"seçtiniz.")

    if secim == "1":
        print("İçecekler kategorisini seçtiniz.")
        urunler.icecekler.icecekmenu()
        urunmenu()
    elif secim =="2":
        print("Meyve kategorisini seçtiniz.")
        urunler.meyveler.meyvemenu()
        urunmenu()
    elif secim =="3":
        print("Sebze kategorisini seçtiniz.")
        urunler.sebzeler.sebzemenu()
        urunmenu()
    elif secim =="4":
        print("Bakliyat kategorisini seçtiniz.")
        urunler.bakliyat.bakliyatmenu()
        urunmenu()
    elif secim =="5":
        print("Süt ürünleri kategorisini seçtiniz.")
        urunler.sut_urunleri.sutmenu()
        urunmenu()
    elif secim =="6":
        print("Temizlik ürünleri kategorisini seçtiniz.")
        urunler.temizlik.temizlikmenu()
        urunmenu()
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")

urunmenu()