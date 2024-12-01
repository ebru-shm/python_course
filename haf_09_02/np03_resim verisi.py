
# boş resim oluşturma
# python -m pip install opencv-python
import cv2
import numpy as np

# aşağıdaki [255, 255, 255] rakamlarını oynayarak ne olduğuna bakın

r1= np.full((50, 200, 3), [255, 0, 255], dtype=np.uint8)
r2= np.full((50, 200, 3), [0, 250, 0], dtype=np.uint8)

print(r1)
cv2.imshow("Olusan resim", r1)
print(r2)
cv2.imshow("Olusan resim", r2)


# birlesik = cv2.hconcat([r1,r2])    # horizontal
birlesik = cv2.vconcat([r1,r2])      # vertical
cv2.imshow("Oluşan Resim3", birlesik)

cevrilmis = cv2.rotate(birlesik, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow("Oluşan Resim4", cevrilmis)

# r1= np.full((200, 300, 3), [255, 255, 255], dtype=np.uint8) # Beyaz
# r2= np.full((200, 300, 3), [0, 0, 0], dtype=np.uint8) # Siyah
# r3= np.full((200, 300, 3), [255, 0, 0], dtype=np.uint8) # Mavi
# r4= np.full((200, 300, 3), [0, 255, 0], dtype=np.uint8) # Yeşil
# r5= np.full((200, 300, 3), [0, 0, 255], dtype=np.uint8) # Kırmızı
# r6= np.full((200, 300, 3), [0, 0, 50], dtype=np.uint8) # Kırmızı (açık)
# r7= np.full((200, 300, 3), [0, 0, 255], dtype=np.uint8) # Kırmızı (yoğun)
# r8= np.full((200, 300, 3), [50, 0, 50], dtype=np.uint8) # Mor (açık)
# r9= np.full((200, 300, 3), [255, 0, 255], dtype=np.uint8) # Mor (yoğun)

# cv2.imshow("Ak", r1)
# cv2.imshow("Gara", r2)
# cv2.imshow("Gok", r3)
# cv2.imshow("Yasil", r4)
# cv2.imshow("Kizil", r5)
# cv2.imshow("Acik kirmizi", r6)
# cv2.imshow("Tam kirmizi", r7)
# cv2.imshow("Acik mor", r8)
# cv2.imshow("Tam mor", r9)

cv2.waitKey(0)
 
cv2.destroyAllWindows()
