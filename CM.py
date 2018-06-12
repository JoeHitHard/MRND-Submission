class CM:
    def __init__(self):
        print("Inside cmFun Method")
        print("Outside cmFun Method")
    def __enter__(self):
        print("Inside Enter method")
        print("Out of Enter Method")
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Inside Exit Method")
        if exc_type!=None:
            print(exc_type, exc_val, exc_tb)
        print("Out of Exit Method")
def test1():
    with CM() as val:
        print("Inside Block")
        print(val)
        i = 2 / 0
        print("Outside Block")
def test2():
    with CM() as val:
        print("Inside Block")
        print("Outside Block")
        print(val)
if __name__=="__main__":
    test1()