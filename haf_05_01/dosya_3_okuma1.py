
# # a = open(f"rehber1.txt","w")  )
# a = open(f"rehber1.txt","w", encoding = "utf8")  # türkçe karakter desteği için utf8
# a.write("Çarş")

a = open(f"rehber1.txt","r") # r = read (eğer mod belirtilmezse yine r kabul edilir.)
a = open(f"dosya_3_okuma1.py", encoding= "utf8")
print(a)
okunan = a.read()
print(okunan)

b = open("print_01.py","r",encoding = "utf8")
print(b)
oku =b.read()
print(oku)


