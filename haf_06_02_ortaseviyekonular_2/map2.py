
urunler = [
    ["Kurşun kalem",40],
    ["Tükenmez kalem",30],
    ["Renkli kağıt",150]
]

kdvOrani = 20

# urunlerKDVli = []
# def kdvEkle(oran):
#     for u in urunler:
#         print(u)
#         yeniUrun = [u[0],u[1]+oran]
#         urunlerKDVli.append(yeniUrun)

urunlerKDVli = list(map(lambda x: [x[0],x[1]+kdvOrani], urunler))



print(urunler)
print(urunlerKDVli)
