chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# for i in range(1, 13):
#     print(i)

for year in range(2010, 2025):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[int(year) % 12]))
