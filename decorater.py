def outer(func):
    def inner(a, b):
        print('decorated!')
        func(a, b)
        return
    return inner
@outer
def minus(c, d):
    print(c - d)
    return

minus(10, 5)

# def outer(func):
#     def inner(a, b):
#         print('decorated!')
#         func(a, b)
#         return
#     return inner

# def minus(c, d):
#     print(c - d)
#     return

# decorate = outer(minus)
# print(decorate)
# decorate(10, 5)