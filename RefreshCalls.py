def blah(func):
    func.count = 0
    func.det = 0
    def wrapper(*args,**key):
        if args[1] == False:
            func(*args, **key)
            return 1
        else:
            func.count = func.count+1
            if func.det == 0:
                func.det = 1
                func(*args, **key)
                i = func.count
                func.count = 0
                func.det = 0
                return i
            else:
                func(*args, **key)
        return 1
    return wrapper
@blah
def factorial(num, recursiveCall):
    if num == 1:
        return 1
    return num * factorial(num - 1, recursiveCall)


print(factorial(3, True))
print(factorial(3, True))
print(factorial(3, False))
print(factorial(3, False))