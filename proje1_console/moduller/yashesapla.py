
def yas_hesaplama():

    dogum_yili = int(input("Lütfen doğum tarihinizi giriniz: "))
    if (dogum_yili <= 2024 or dogum_yili > 0):
        yas = 2024 - dogum_yili
        print(f"Yaşınız {yas}.")
    else:
        print("Lütfen geçerli bir dogum yili giriniz. ")




    
