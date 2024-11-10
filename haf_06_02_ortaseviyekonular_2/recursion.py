
# kendi kendini çağıran fonksiyonlar recursive olarak adlandırılır.

# sayac = 0
# def biteneKadarHarca(para):
#     global sayac
#     sayac += 1  
#     harcanan = para*.1
#     kalan = para - harcanan
#     print("Paranız: ", para,"Harcanan: ", harcanan, "Kalan: ", kalan)
#     # kalan > 10: biteneKadarHarca(kalan)    # recursive fonksiyonlarda ne kadar çalışacağı belirtilmelidir. Yoksa python yorumlayıcısı hafıza için bu işlemi sonlandırır.
#     if kalan > 10: biteneKadarHarca(kalan)    

# biteneKadarHarca(1000)
# print(f"Paranız {sayac} harcama sonunda 10 lira kalmış oldu.")


# sayac1 = 5
# def kalk():
#     global sayac1
#     sayac1 += 1
#     print(f"... zamanında kalkıldı.")
#     if sayac1 < 20: kalk()             # if ile şart yoksa python yorumlayıcısı hafıza için bu işlemi sonlandırır.
#     kalk()

# kalk()