def multiply(x,y):
    result=0
    for i in range(y):
        result=result+x
    return result

print(multiply(5,3))


def exponential(x,y):
    result=1
    for i in range(y):
        result=result*x
    return result

print(exponential(5,3))

def square(x):
    return exponential(x,2)

print(square(4))