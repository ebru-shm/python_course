import moduller.hesap
import moduller.string
import moduller.cizim
import moduller.faktoriyel
import moduller.liste
import moduller.yashesapla
import moduller.python_kutuphane
import moduller.alan_hesapla
import moduller.urun_oneri
import moduller.kilo_indeks

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
    print("║  5-Liste İşlemleri       ║")
    print("║  6-Yaş Hesaplama         ║")
    print("║  7-Python Kütüphaneleri  ║")    
    print("║  8-Alan Hesaplama        ║")
    print("║  9-Ürün Önerileri        ║")
    print("║  10-Kilo İndeksi         ║")
    print("║  Çıkış (q)               ║")
    print("║                          ║")
    print("║                          ║")
    print("║      Seçiminiz?          ║")
    print("╚══════════════════════════╝")

    secim = input("işlem yapmak istediğiniz kategoriyi seçiniz: ")


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
        islemmenu()
    elif secim =="4":
        print("Faktoriyel bulma kategorisini seçtiniz.")
        moduller.faktoriyel.faktoriyel_hesap()
        islemmenu()
    elif secim =="5":
        print("Liste işlemleri kategorisini seçtiniz.")
        moduller.liste.liste_islem()
        islemmenu()
    elif secim =="6":
        print("Yaş hesaplama kategorisini seçtiniz.")
        moduller.yashesapla.yas_hesaplama()
        islemmenu()
    elif secim =="7":
        print("Python kütüphaneleri kategorisini seçtiniz.")
        moduller.python_kutuphane.kutuphane()
        islemmenu()
    elif secim =="8":
        print("Alan hesaplama kategorisini seçtiniz.")
        moduller.alan_hesapla.alan_hesaplama()
        islemmenu()
    elif secim =="9":
        print("Ürün önerileri kategorisini seçtiniz.")
        moduller.urun_oneri.model_oneri()
        islemmenu()
    elif secim =="10":
        print("Kilo indeksi kategorisini seçtiniz.")
        moduller.kilo_indeks.kilo_indeksi()
        islemmenu()
    elif secim =="q":
        exit()
    else:
        print("Hatalı giriş yaptınız, lütfen tekrar giriniz.")

islemmenu()