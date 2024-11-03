

def rehber_ekle():
    dosya= open("rehber.txt","a")
    print("\n\n Rehbere eklenecek bilgileri giriniz: ")
    ad = input("Ad: ")
    tel = input("Tel: ")
    dosya.write(f"{ad}#{tel}\n")
    dosya.close()
    print("\n\nRehberdekiler (yeni şekli):")
    rehber_listele()

def rehber_listele():
    print("\n\nRehberiniz: ")
    dosya = open("rehber.txt")
    okunan = dosya.readlines()
    # print(okunan)
    for sira,a in enumerate(okunan):
        b = a.split("#")
        # print(sira+1 ,"-", b[0],"\tTelefonu:",b[1])
        print(f"{sira+1} - {b[0]},\t Telefonu: {b[1]}")
    dosya.close()
 
def rehber_sil(): 
    print("Mevcut Kayıtlar")
    # rehber_listele()
    silinecek= input("Hangi kayıt silinecek(numarasını girin): ")
    dosya = open("rehber.txt","r")
    okunan = dosya.readlines()
    print(okunan)
    for s, a in enumerate(okunan):
        print(s,a)
        if s!= silinecek: dosya.write(a)
    dosya.close()

    # dosya.close()
    # dosya = open("rehber.txt","w")

    # for sira,a in enumerate(okunan):
    #     if sira!= silinecek: dosya.write(a)
    
    # dosya.close()


def rehber_düzenle(): 
    pass


def anamenu():
    
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║  REHBER UYGULAMASI  ║")
    print("║                     ║")
    print("║  1-Kişi ekle        ║")
    print("║  2-Kişi listesi     ║")
    print("║  3-Kişi Düzenle     ║")
    print("║  4-Kişi Silme       ║")
    print("║  5-Çıkış            ║")
    print("║                     ║")
    print("║  Seçimiz nedir?     ║")
    print("╚═════════════════════╝")
    # 201 ╔ 187 ╗ 200 ╚  # 188 ╝

    secim = input ("Seçiminiz: ")
    
    if secim =="1": rehber_ekle(); anamenu()
    elif secim =="2": rehber_listele(); anamenu()
    elif secim =="3": rehber_sil(); anamenu()
    elif secim =="4": rehber_düzenle(); anamenu()
    elif secim =="5": rehber_ekle(); anamenu()
        
        
anamenu()


