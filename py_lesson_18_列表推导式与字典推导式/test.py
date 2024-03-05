# 计算 1 ～ 10 所有偶数的平方
alist = []
for i in range(1, 11):
    if i % 2 == 0:
        alist.append(i * i)
print(alist)

# 列表推导式
blist = [i * i for i in range(1, 11) if i % 2 == 0]
print(blist)

zodiac_name = (
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius',
    'Pisces')
adict = {}
for z in zodiac_name:
    adict[z] = 0

bdict = {i: 0 for i in zodiac_name}
