
# Lambda fonk. tek satırlık basit (anonim) fonksiyonlardır. Amaç tek satırlık fonksiyonları kolayca yazabilmektir.

#*** Klasik yöntem ile

# def kareAl (a):
#     return a**2
# print(kareAl(5))


#*** Lambda ile 1
# print((lambda x:x**2)(5))


#*** Lambda ile 2
karesiniAl = lambda x:x**2
print(karesiniAl(5))

