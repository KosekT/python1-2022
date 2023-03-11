def add(a, b):
    return a+b

def mul(a, b):
    return a*b

def calculate(fn, a, b):
    fun = f'{fn}({a},{b})'
    # return exec(fun)
    match fn:
        case "add":
            return add(a,b)
        case "mul":
            return mul(a,b)
    


print(calculate("add", 3, 4))