

dosya = open("C:/Users/vektorel/Desktop/Ebru/haf_05_02/tekrar_dosya2.py","r")

okunan = dosya.read(10)   
print(okunan)

okunan = dosya.read(10) 
print(okunan)

okunan = dosya.read(10) 
print(okunan)

dosya.seek(0,0)
okunan = dosya.read(10)
print(okunan)



# yer = dosya.tell(); # pozisyon bilgisi
# print("Şu anki pozisyon: ",yer)
# yer = dosya.seek(2,0); # satır ve karakter
# yer = dosya.tell();    # pozisyon bilgisi