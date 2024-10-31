
import turtle

def kare():
    for a in range(4):
        turtle.forward(100)
        turtle.right(90)

def dikdortgen():
    for a in range(2):
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)

def ucgen():
    for a in range(3):
        turtle.forward(100)
        turtle.right(120)
        

def besgen():
    for a in range(5):
        turtle.forward(100)
        turtle.right(72)     
                
def altigen():
    for a in range(6):
        turtle.forward(100)
        turtle.right(60)


def cizim_yap():
      
    print("\033[1;32;40m")                     
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    #print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║         ÇİZİM       ║")
    print("║                     ║")
    print("║  1-Kare             ║")
    print("║  2-Dikdörtgen       ║")
    print("║  3-Üçgen            ║")
    print("║  4-Beşgen           ║")
    print("║  5-Altıgen          ║")
    print("║                     ║")
    print("║                     ║")
    print("║    Seçimiz nedir?   ║")
    print("╚═════════════════════╝")

    secim = input("Yapmak istediğiniz işlem: ")


    if secim == "1": 
        kare()
    elif secim == "2":
        dikdortgen()
    elif secim == "3":
        ucgen()
    elif secim == "4":
        besgen()
    elif secim == "5":
        altigen()
    else:
        print("Yanlış seçim yaptınız. Lütfen tekrar deneyiniz.")