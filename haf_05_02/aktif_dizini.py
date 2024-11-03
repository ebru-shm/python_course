
import os
calısma_dizini = os.getcwd() # current work
print("Aktif dizin:",calısma_dizini)

print("\n\nAktif dizidekilerin listesi:\n")
xyz = os.listdir()     # mevcut konumdaki dosya ve dizinlerin dizi olarak listesi.

for a in xyz:
    print(a,end="")
    if os.path.isfile(a): print("\t\t (Dosya)")
    else: print("\t\t (Klasör)")
