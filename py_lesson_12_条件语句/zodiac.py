chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

year = input('请用户输入年份: ')
zodiac = chinese_zodiac[int(year) % 12]
print('今年的生肖是：', zodiac)
if zodiac == '龙':
    print("龙年大吉")
