file1 = open('name.txt')
# print(file1.readline())

# for line in file1.readlines():
#     print(line)
#     print('---------')
#
# file1.close()

print('当前文件指针的位置:%d' % file1.tell())  # 0 文件指针
print('当前读取到了一个字符，字符的内容是 %s' % file1.read(1))
print('当前文件指针的位置:%d' % file1.tell())
file1.seek(0)
print('当前文件指针的位置:%d' % file1.tell())
print('当前读取到了一个字符，字符的内容是 %s' % file1.read(1))
print('当前文件指针的位置:%d' % file1.tell())
print('当前读取到了一个字符，字符的内容是 %s' % file1.read(1))
print('当前文件指针的位置:%d' % file1.tell())
file1.close()
