def add (a, b):
    sum = a + b
    return sum

def mul (a, b):
    il = a * b
    return il

def calculate(fn, a, b):
    if (fn == add):
        return add(a, b)
        
    elif (fn == mul):
        return mul(a , b)
    
    return  0

print (calculate(mul, 2, 5))