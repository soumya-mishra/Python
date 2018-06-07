def gen1():
    for char in "Python":
        yield char
    for i in range(5):
        yield i

def gen2():
    yield from "Python"
    yield from range(5)

g1 = gen1()
g2 = gen2()
print("g1: ", end=", ")
for x in g1:
    print(x, end=", ")
print("\ng2: ", end=", ")
for x in g2:
    print(x, end=", ")
print()

#The yield from <expr> statement can be used inside the body of a generator.
#<expr> has to be an expression evaluating to an iterable,
# from which an iterator will be extracted. 
#The iterator is run to exhaustion, i.e. until it encounters a StopIteration exception.
# This iterator yields and receives values to or from the caller of the generator,
# i.e. the one which contains the yield from statement. 
