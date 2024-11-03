
# import os

# l = os.walk("D:\\")
# print(l)

# for a in l:
#     print(a)

#********* alttaki kodda içinde rehber adı geçen klasör var mı diye bakıyoruz.

import os
from os.path import join, getsize

for xx, klasor, dosyalar in os.walk('D:\\'):
    print(xx, "consumes", end="")
    print(sum(getsize(join(xx, name))
    for name in dosyalar), end="")
    print("bytes in", len(dosyalar), "non-directory files")
    if 'REHBER' in klasor:
        klasor.remove('REHBER') # don't visit CVS directories

