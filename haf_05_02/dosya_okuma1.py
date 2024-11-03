
dosya = open("C:/Users/vektorel/Desktop/Ebru/haf_05_02/tekrar_dosya2.py","r")

okunan = dosya.read()  # tüm dosya içeriğini oku.
okunan = dosya.read(10)  # dosyadan 10 karakter oku.
print(okunan)

okunan = dosya.readlines()  # dosyadan satırlar olarak oku.
print(okunan)

print("\n\n Okunan 3.index:",okunan[4])