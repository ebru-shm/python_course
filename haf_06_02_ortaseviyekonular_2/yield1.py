
def sayac():
    i= 0;
    while True: 
        yield i; 
        i +=1

say = sayac()
print(*say)

