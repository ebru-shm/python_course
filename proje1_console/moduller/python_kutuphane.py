
def kutuphane():

    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════ ╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║ PYTHON KÜTÜPHANELERİ ║")
    print("║                      ║")
    print("║  1-Numpy             ║")
    print("║  2-Pandas            ║")
    print("║  3-Matplotlib        ║")
    print("║  4-Seaborn           ║")
    print("║  5-TensorFlow        ║")
    print("║                      ║")
    print("║                      ║")
    print("║    Seçimiz nedir?    ║")
    print("╚══════════════════════╝")


    
    secim = input ("Bilgi almak istediğiniz kütüphaneyi seçiniz: ")

    if secim == "1":
        print("Numpy-(Numerical Python), çok boyutlu dizilerle ve matrislerle çalışmamızı sağlayan")
        print("ve matematiksel işlemler yapabileceğimiz bir Python dili kütüphanesidir. Bu kütüphane,")
        print("vektör ve matris işlemleri için gerekli olan çeşitli araçları sağlar.")

    elif secim =="2":
        print("Pandas, Python programlama dilinde geliştirilen güçlü bir veri analizi ve manipülasyon kütüphanesidir.")
        print("Adını “panel data” teriminden alır ve özellikle tablo benzeri verileri işlemek için tasarlanmıştır.")
        print("Pandas, temel olarak iki ana veri yapısı olan Series ve DataFrame’i sunar. Series, tek boyutlu verileri,")
        print("DataFrame ise çok boyutlu tablo benzeri verileri temsil eder. Bu yapılar, verilerin saklanması,")
        print("işlenmesi ve analiz edilmesi için güçlü araçlar sunar.")

    elif secim =="3":
        print("Matplotlib; veri görselleştirmesinde kullandığımız temel python kütüphanesidir. 2 ve 3 boyutlu çizimler yapmamızı sağlar.")
        print("Matplotlib genelde 2 boyutlu çizimlerde kullanılırken, 3 boyutlu çizimlerde başka kütüphanelerden yararlanılır.")

    elif secim =="4":
        print("Seaborn, Python programlama dilinde kullandığımız bir veri görselleştirme kütüphanesidir. Veri görselleştirme sürecini")
        print("kolaylaştırmak için önceden tanımlanmış stiller ve renk paletleri sağlar.")

    elif secim =="5":
        print("TensorFlow, Google tarafından geliştirilen ve açık kaynak olarak sunulan bir makine öğrenimi kütüphanesidir. Bu kütüphane,")
        print("kullanıcıların model oluşturma, eğitme ve uygulama işlemlerini gerçekleştirmek için gereken araçları sağlar.TensorFlow, makine")
        print("öğrenimi, derin öğrenme ve yapay zeka gibi alanlarda yaygın olarak kullanılmaktadır.")

    else:
        print("Yanlış bir giriş yaptınız, lütfen tekrar seçim yapınız.")