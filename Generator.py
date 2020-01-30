#Generator example 1
def fibonacci(n):
    """ A generator for creating the Fibonacci numbers """
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5)
for x in f:
    print(x, " ", end="") # 
print()
#Use of exception and retun in generator
def gen():
    yield 1
    raise StopIteration(42)
 
g = gen()
next(g)    
next(g)

#
#Traceback (most recent call last):
#  File "", line 1, in 
#  File "", line 3, in gen
#StopIteration: 42 
######################
Use of Return
>>> def gen():
...     yield 1
...     return 42
... 
>>> 
>>> g = gen()
>>> next(g)
1
>>> next(g)
Traceback (most recent call last):
  File "", line 1, in 
StopIteration: 42
>>> 
######################
#Genrators with send 
#########
>>> def simple_coroutine():
...     print("coroutine has been started!")
...     x = yield 
...     print("coroutine received: ", x)
... 
>>> cr = simple_coroutine()
>>> cr

>>> next(cr)
##############
#Throw method
################
class StateOfGenerator(Exception):
     def __init__(self, message=None):
         self.message = message

def infinite_looper(objects):
    count = 0
    while True:
        if count >= len(objects):
            count = 0
        try:
            message = yield objects[count]
        except StateOfGenerator:
            print("index: " + str(count))
        if message != None:
            count = 0 if message < 0 else message
        else:
            count += 1
   
  #Method call
  >>> from generator_throw import infinite_looper, StateOfGenerator
>>> looper = infinite_looper("Python")
>>> next(looper)
'P'
>>> next(looper)
'y'
>>> looper.throw(StateOfGenerator)
index: 1
't'
>>> next(looper)
'h'
>>> 

