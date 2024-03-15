# iter
list1 = [1, 2, 3]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))

# range
for i in range(10, 20, 2):
    print(i)


# yield 生成器
def custom_range(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in custom_range(10, 20, 0.5):
    print(i)
