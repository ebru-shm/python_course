
import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)  # sys.argv uygulamanın dışarıdan (windows gibi) parametre almasını sağlamak için kullanılır.

window = QMainWindow()
window.show()
# Start the event loop.

window1 = QWidget()
window1.show()  


app.exec()
