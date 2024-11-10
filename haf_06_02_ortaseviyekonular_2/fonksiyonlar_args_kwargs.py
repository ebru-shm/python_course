
# def selamla(gelen):
#     print(gelen)
#     gelen.append("Nur")
#     for a in gelen:
#         print("Merhaba",a)


# ogrenciler = ["Ali","Can","Cem"]
# selamla(ogrenciler)


def selamla(*gelen):        # args argümanlar = parametreler = fonksiyonun kullandığı değişkenler
    # gelen.append("Nur")   # tuple olarak aldığından dolayı ekleme yapamayız.
    print(gelen)
    print("Gelen[1]:",gelen[1])
    for a in gelen:
        print("Merhaba",a)


selamla("Ali","Can","Cem")