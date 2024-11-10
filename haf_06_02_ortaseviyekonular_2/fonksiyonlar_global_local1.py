
x = 50
def fonksiyon1(a):
    global x
    print("1.Durum=",a)
    print("2.Durum=",x) # global x olduğundan x=.. dan önce kullanılabilir
    x=100
    print("3.Durum=",x)
fonksiyon1(20)
print("4.Durum=",x)