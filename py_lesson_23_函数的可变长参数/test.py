# print('abc', end='\n\n')
# print('abc')


def func(a, b, c):
    print('a = %s' % a)
    print('b = %s' % b)
    print('c = %s' % c)


func(1, 2, 3)
func(1, c=2, b=3)


# 取参数的个数
def howlong(first, *other):
    print('参数的长度为：', 1 + len(other))


howlong(123, 234, 456)
howlong(123)
