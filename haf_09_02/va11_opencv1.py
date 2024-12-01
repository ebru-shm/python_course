
# Ör-3: Kameradan görüntü al
import cv2
vid = cv2.VideoCapture(0)
while True:
    ret, kare = vid.read()
    cevrilmis = cv2.rotate(kare, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('pencere',kare)
    cv2.imshow('pencere1',cevrilmis)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.relase()
# cv2.destroyWindow('pencere')
cv2.destroyAllWindows() 

# waitKey(1) == ord('q') # çalışmazsa
# waitKey(1) & 0xFF == ord('q') # kullan
# Bu platform ile ilgili bir konu
