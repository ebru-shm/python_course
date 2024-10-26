
meyveler1 = ["muz","nar","dut"]        # list turu collection
meyveler2 = ["elma","armut","kivi"]    # tuple turu collection
meyveler3  = ["havuç","portakal","greyfurt"]
meyveler2 =()

print(meyveler1)
print(meyveler2)

print(type(meyveler1))
print(type(meyveler2))

# print(meyveler1+meyveler2) tipleri aynı olmadığından hata verir.

m4 = meyveler1 + meyveler3
print(m4)

meyveler1 += meyveler3
m4 = meyveler1 + meyveler3
print(m4)

print(meyveler1)

meyveler1.append("karpuz")
print(meyveler1)

meyveler1.insert(1,"Bostan")
print(meyveler1)

meyveler1.append(["karpuz","çilek"])   # liste sonuna eleman ekler.
print(meyveler1)

meyveler3.insert(3,"Mandalina")  # istenilen yere eleman ekler.
meyveler3

yenimeyveler = ["nar","muz"]
meyveler1.extend(yenimeyveler)
print(meyveler1)

meyveler1.pop()  # son elemanı siler.
print(meyveler1)

