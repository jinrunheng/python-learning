import re


def find_item(s: str) -> int:
    with open('1.txt') as f:
        data = f.read()
    return len(re.findall(s, data))


with open('2.txt') as f:
    i_dict = {}
    data = f.read()
    items = data.split("|")
    for i in items:
        i_num = find_item(i)
        i_dict[i] = i_num
# 按照出现次数从大到小排序
i_dict_sorted = sorted(i_dict.items(), key=lambda x: x[1], reverse=True)
print(i_dict_sorted)
