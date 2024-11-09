
def topla(*degerler): # degerler[, , , ,]
    # print(degerler) # tuple içine atılan parametre değerleri
    toplam = 0
    for a in degerler:
    #   print(a)
        toplam += a
    print(toplam)
    return toplam

# topla()

def carp(*d): # degerler[, , , ,]
    # print(degerler)
    sonuc = 1
    for a in d: sonuc *= a
    print(sonuc)
    return sonuc

bb = topla(2,1,3,5)
print(bb)

cc = carp(2,1,3,5)
print(cc)