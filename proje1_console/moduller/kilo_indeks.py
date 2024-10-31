
def kilo_indeksi():

    kilo = float(input("Kilogram cinsinden ağırlığınızı giriniz: "))
    boy = float(input("Metre cinsinden boyunuzu giriniz: "))

    vki = kilo / (boy**2)

    print(f"Vücut kitle indeksiniz: {"%.1f" % vki} ")

    if (vki < 18.5): print("Zayıf")
    elif (vki >= 18.5 and vki < 24.9): print("Sağlıklı")
    elif (vki >= 25 and vki < 29.9): print("Şişman")
    elif (vki >= 30 and vki < 39.9): print("Obez")
    else: print("Girdiğiniz değerleri kontrol ediniz. ")





