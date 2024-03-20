def counter(n=0):
    cnt = [n]

    def add_one():
        cnt[0] += 1
        return cnt[0]

    return add_one


# num_add = counter(10)
num_add = counter(10)
print(num_add())
print(num_add())
print(num_add())
print(num_add())
print(num_add())
