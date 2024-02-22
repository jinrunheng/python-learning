zodiac_name = (
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius',
    'Pisces')

print((4) > (5))  # False
print((3, 19) < (4, 2))  # true；元组的大小比较是通过字典序进行比较的
# filter
a = (1, 3, 5, 7)
b = 4
c = filter(lambda x: x < b, a)
for f in c:
    print(f)

print(
    len(list(c)))  # 为什么会输出 0？因为当 for 循环结束后，c 迭代器已经被耗尽，没有更多的元素可以迭代了，所以最后一行尝试将 c 转换为列表并获取其长度，但由于迭代器已经被耗尽，所以得到的列表是空的，长度为 0

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23),
               (12, 23))
(month, day) = (4, 14)
# 打印出 zodiac_days 中所有小于 (month, day) = (4, 14) 的元组
zodiac_day = filter(lambda x: x < (month, day), zodiac_days)
zodiac_list = list(zodiac_day)
for i in zodiac_list:
    print(i)

zodiac_len = len(zodiac_list) % 12
print("your zodiac is :", zodiac_name[zodiac_len])
