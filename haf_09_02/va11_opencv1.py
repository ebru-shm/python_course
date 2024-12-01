
# Ör-3: Kameradan görüntü al
import cv2
vid = cv2.VideoCapture(0)
while True:
    ret, kare = vid.read()
    cv2.imshow('pencere',kare)
    cevrilmis = cv2.rotate(kare, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('pencere1',cevrilmis)

    bulanik = cv2.GaussianBlur(kare,(7,7),0)
    cv2.imshow('pencere2',bulanik)

    hsvSekli = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)
    cv2.imshow('pencere3',hsvSekli)

    sbSekli = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)  # siyah beyaz
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.relase()
# cv2.destroyWindow('pencere')
cv2.destroyAllWindows() 

# waitKey(1) == ord('q') # çalışmazsa
# waitKey(1) & 0xFF == ord('q') # kullan
# Bu platform ile ilgili bir konu
