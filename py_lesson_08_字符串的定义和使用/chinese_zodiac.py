# 记录生肖，根据年份来判断生肖
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

year = input()
print(chinese_zodiac[int(year) % 12])
