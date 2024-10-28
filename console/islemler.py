import moduller.hesap
import moduller.string
import moduller.cizim

def islemmenu():

    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔══════════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║         İŞLEMLER         ║")
    print("║                          ║")
    print("║  1-Hesaplamalar          ║")
    print("║  2-String İşlemleri      ║")
    print("║  3-Çizimler              ║")
    print("║  4-Faktoriyel Bulma      ║")
    print("║  5-Yaş Hesaplama         ║")
    print("║  6-Şifre Kontrolü        ║")    
    print("║  7-Telefon Markalari     ║")
    print("║  8-Gezi Rehberi          ║")
    print("║                          ║")
    print("║                          ║")
    print("║  Seçimiz nedir?          ║")
    print("╚══════════════════════    ╝")

    secim = input("işlem yapmak istediğiniz kategoriyi seçiniz: ")

    print(secim,"seçtiniz.")

    if secim == "1":
        print("Hesaplamalar kategorisini seçtiniz.")
        moduller.hesap.hesaplama()
        islemmenu()
    elif secim =="2":
        print("String işlemleri kategorisini seçtiniz.")
        moduller.string.stringislem()
        islemmenu()
    elif secim =="3":
        print("Çizimler kategorisini seçtiniz.")
        moduller.cizim.cizim_yap()
    #     islemmenu()
    # elif secim =="4":
    #     print("Faktoriyel Bulma kategorisini seçtiniz.")
    #     urunler.bakliyat.bakliyatmenu()
    #     islemmenu()
    # elif secim =="5":
    #     print("Yaş Hesaplama kategorisini seçtiniz.")
    #     urunler.sut_urunleri.sutmenu()
    #     islemmenu()
    # elif secim =="6":
    #     print("Şifre Kontrolü kategorisini seçtiniz.")
    #     urunler.temizlik.temizlikmenu()
    #     islemmenu()
    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")

islemmenu()