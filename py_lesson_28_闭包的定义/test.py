def func():
    a = 1
    b = 2
    return a + b

# 闭包
def sum(a):
    def add(b):
        return a + b
    return add

sum_func = sum(2)
sum = sum_func(4)
print(type(sum_func))
print(type(sum))
print(sum)