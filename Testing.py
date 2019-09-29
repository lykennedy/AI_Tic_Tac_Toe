def func1(func):
    def wrapper():
        func()
        print("The function passed in will be executed above.")
    return wrapper


@func1
def func2():
    print("Yall be sucking dick")


func2()
