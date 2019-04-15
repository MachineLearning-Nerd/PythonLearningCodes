from time import time 
def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('Elasped Time:',after-before)
        return rv
    return f
    
@timer
def add(x=20, y=10):
    return x + y


print("add(10,20): " , add(10,20))
print("add(10,20): " , add(20,10))
print("add(10,20): " , add(30,50))
print("add(10,20): " , add(40,40))