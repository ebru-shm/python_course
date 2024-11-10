
# meyveler = ["muz","dut","nar","elma","armut","kiraz","çir"]
# print(meyveler)

# print(sorted(meyveler))

# meyveler.sort()
# print(meyveler)

# meyveler.sort(reverse = True)
# print(meyveler)

# if "dut" in meyveler: print("nar")
# else: print("Yok")


import random
sayilar = []
max = 1000

print("Atama işlemi başladı.")
for a in range(max):
    sayilar.append(random.randint(1,max))


print("Yazdırma işlemi başladı.")
print(sayilar)

print("Sıralama işlemi başladı.")
sayilar.sort()

print("Sıralanmışları yazdırma işlemi başladı.")
print(sayilar)





