meyveler1 = ["muz","dut","nar"] # list turu collection
meyveler2 = ("elma","armut","kivi") # tuple turu collection
meyveler3 = ["havuz","portakal","greyfurt"] 
 
print(meyveler1)
print(meyveler1)

print(type(meyveler1))
print(type(meyveler2))

# print(meyveler1+meyveler2) # tipleri aynı olmadığından hata verir
# print(meyveler1+meyveler3)
meyveler1 += meyveler3
m4 = meyveler1+meyveler3
print(m4)

print(meyveler1)

meyveler1.append("karpuz") # liste sonuna elaman ekler.
print(meyveler1)

# meyveler2.append("karpuz") # tuplelara ekleme yapılamaz.

meyveler1.insert(1,"Bostan") # istenilen yere eleman ekler
print(meyveler1)

meyveler1.pop() # son elemanı siler 
print(meyveler1)

print(meyveler1[2:])
print(meyveler1[:2])
print(meyveler1[2:6])
print(meyveler1[2:6:2])

# print(meyveler1)
# yenidizi = meyveler1.sort()
# print(yenidizi)

print(len(meyveler1))



