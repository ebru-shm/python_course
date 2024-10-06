m1 = "Şehirler"
m2 = "Ankara"
m3 = "izmir"
m4 = f"İller {m3} -- {m2}"
m5 = f"{m1} {m4} {m2}"
m6 = "Şehirler: {}, {}".format(m2,m3)
m7 = "Şehirler: %s, %s" %(m2,m3)
print(m4)
print(m5)

# pythonda string formatlama(metin şekillendirme işlemi)
print(f"Şehirler: {m2},{m3}")
print(f"{m3} bir şehirdir.")
print("Şehirler: {}, {}".format(m2,m3))
print("Şehirler: %s, %s" %(m2,m3))

print(m6)
print(m7)

