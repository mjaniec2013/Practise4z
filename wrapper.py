
# decorators / wrappers

from time import time
from time import sleep
import random

def random_wait():
    sleep( random.random() )

def timer(fun, random_time=True):

    def wrap(*args, **kwargs):
        t0  = time()
        res = fun(*args, **kwargs)
        if random_time: random_wait()
        t1  = time()
        print("elapsed= %0.10f" % float(t1-t0))
        return res
    return wrap

@timer
def add(x, y=10):
    return x+y
# add = timer( add )

@timer
def strange(x, y, z):
    return round( pow(x, random.random()*3)-pow(y, random.random()*2)+pow(z, random.random()*4), 4)
# strange = timer( strange )

print( "add=\t",   add(20) )
print( "strange=", strange(1.0, 3.2, 5.4) )
