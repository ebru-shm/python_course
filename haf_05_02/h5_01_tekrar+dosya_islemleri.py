
# open("deneme","w")

import os
import time
# ka = input("Klasör adı: ")
# os.mkdir(ka)

# for a in range(10):
#     open(f"virus{a}.bat","a")  # w dosyanın içindeki tüm bilgileri silip tekrar açıyor. Bu yüzden 10 tane açmadı, 1 tane açtı.
    #   print(f"virus{a}.bat")


# for a in range(10):
#     os.remove(f"virus{a}.bat")

# for a in range(2,10):
#     time.sleep(1)
#     open(f"virus{a}.bat","a")
#     b = a - 2
#     os.remove(f"virus{b}.bat")

# open("arcelik_faturalari.txt","r")
# open("arcelik_faturalari.txt","r").read()
# okunan = open("arcelik_faturalari.txt","r").read()

# print(okunan)

dosya = open("arcelik_faturalari.txt","r+")
okunan = dosya.read()
print(okunan)

dosya.write("\n2024-11-03 12500TL")
okunan = dosya.read()
print(okunan)