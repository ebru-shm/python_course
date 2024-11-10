
sayilar = [11,20,3,6,7]
print(sayilar)


# def tekMi (xx):
#     return xx%2 ==1

# yeniDizi = list(filter(tekMi,sayilar))  # tek değer gönderirken fonksiyon parametresiz yazılır.

# yeniDizi = list(filter(lambda x: True, sayilar))

yeniDizi = list(filter(lambda x: x%2 == 1, sayilar))

print(yeniDizi)