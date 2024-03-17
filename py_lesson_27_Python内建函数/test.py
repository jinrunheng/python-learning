# filter
a = [1, 2, 3, 4, 5, 6, 7]
# 过滤出所有的偶数
b = list(filter(lambda x: x % 2 == 0, a))
print(b)
# map
a2 = [1, 2, 3, 4, 5, 6, 7]
b2 = list(map(lambda x: x * 2, a2))
print(b2)
# reduce
from functools import reduce

print(reduce(lambda x, y: x + y, [2, 3, 4], 1))  # 10
print(reduce(lambda x, y: x * y, [3, 4, 5], 2))  # 120

# zip
c = (1, 2, 3)
d = (4, 5, 6)
for i in zip(c, d):
    print(i)
# zip 的典型应用, 字典 k,v 对调
a_dict = {'a': 'aaa', 'b': 'bbb', 'c': 'ccc'}
a_reverse_dict = dict(zip(a_dict.values(), a_dict.keys()))
print(a_reverse_dict)
