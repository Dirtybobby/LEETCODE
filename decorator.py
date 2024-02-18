
def outer(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    print("Some message")
    return inner


@outer
def div(a, b):
    return a / b

print(int(div(4, 2)))

