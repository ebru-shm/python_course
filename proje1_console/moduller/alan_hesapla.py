
import numpy as np
    
def alan_hesaplama():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔════════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║      ALAN HESAPLAMA    ║")
    print("║                        ║")
    print("║  1-Kare                ║")
    print("║  2-Dikdörtgen          ║")
    print("║  3-Üçgen               ║")
    print("║  4-Çember              ║")
    print("║  5-Silindir            ║")
    print("║                        ║")
    print("║                        ║")
    print("║    Seçimiz nedir?      ║")
    print("╚════════════════════════╝")



    secim = input("Yapmak istediğiniz işlemi seçiniz: ")           

    if secim == "1":
        print("Seçilen İşlem: Kare Alan Hesaplama")
        a = int(input("Karenin bir kenarının ölçüsünü giriniz: "))
        k_alan = a**2
        print(f"Karenin alanı = {k_alan}")

    elif secim =="2":
        print("Seçilen İşlem: Dikdörtgen Alan Hesaplama")
        uzun_kenar = int(input("Dikdörtgenin uzun kenar ölçüsü: "))
        kisa_kenar = int(input("Dikdörtgenin kısa kenar ölçüsü: "))
        d_alan = uzun_kenar*kisa_kenar
        print(f"Dikdörtgenin alanı = {d_alan}")

    elif secim =="3":
        print("Seçilen İşlem: Üçgen Alan Hesaplama")
        taban_kenar = int(input("Üçgenin taban kenar ölçüsü: ")) 
        yukseklik = int(input("Yükseklik: "))
        u_alan = (taban_kenar*yukseklik)/2
        print(f"Üçgenin alanı = {"%.2f" % u_alan}")

    elif secim =="4":
        print("Seçilen İşlem: Çember Alan Hesaplama")
        r = int(input("Çemberin yarıçapı: "))
        c_alan = np.pi*(r**2)
        print(f"Çemberin alanı = {"%.2f" % c_alan}")


    elif secim =="5":
        print("Seçilen İşlem: Silindir Alan Hesaplama")
        r = int(input("Yarıçap: "))
        h = int(input("Yükseklik: "))
        s_alan = 2*np.pi*(r**2) + 2*np.pi*r*h
        print(f"Silindirin alanı = {"%.2f" % s_alan}")

    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")