def pi(a):
    def calc(radius):
        print(radius * radius * a)
        return
    return calc

a = pi(3.141592)
b = pi(3.14)
c = pi(3)

a(5)
b(5)
c(5)