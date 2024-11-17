

from PyQt6.QtWidgets import *
uyg = QApplication([])


pencere = QWidget()
pencere.show() 

window1 = QWidget()
window1.show()  

xx = QWidget()
xx.show()

# 3 tane pencere oluşturmuş olduk.

uyg.exec()   # exec() metodu uygulamayı çalışır durumda tutar.

print("Birinci uyg bitti ikinciye geçiliyor.")

uyg1 = QApplication([])
yy = QWidget()
yy.show()
uyg1.exec() 





