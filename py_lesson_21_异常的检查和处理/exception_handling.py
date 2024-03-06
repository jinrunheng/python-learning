# try:
#     i = 100
#     j = i / 0
# except ZeroDivisionError as e:
#     print('0 不能作为除数 %s' % e)
#
# try:
#     year = int(input('input year：'))
# except Exception as e:
#     print('年份要输入数字！')
# try:
#     raise NameError('helloError')
# except NameError as e:
#     print('myCustom error')

a = None
try:
    a = open('name1.txt')
except Exception as e:
    print(e)
finally:
    if a is not None:
        a.close()
