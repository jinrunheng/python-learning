# open() 打开文件
# read() 输入
# readline() 输入一行
# seek() 文件内移动
# write() 输出
# close() 关闭文件
# 将小说的主要人物记录在文件中
# open -> write -> close
file = open('name.txt', 'w')
file.write('诸葛亮\n')
file.close()
# 增加写入
file3 = open('name.txt', 'a')
file3.write('刘备\n')
file3.close()
# 读取文件
file2 = open('name.txt')
context = file2.read()
print(context)
file2.close()
