zodiac_name = (
    'Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius',
    'Pisces')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23),
               (12, 23))
# 用户输入月份与日期
month = int(input("请输入月份："))
day = int(input("请输入日期："))
n: int = 0
if month == 12 and day > 23:
    print(zodiac_name[n])
else:
    while zodiac_days[n] < (month, day):
        n += 1
    print(zodiac_name[n])
