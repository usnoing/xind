import random
def max_list(alist):
    # 创建副本，不修改原列表
    sorted_list = alist.copy()
    n = len(sorted_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
                swapped = True
        if not swapped:
            break
    return sorted_list
            

s = []
changdu = random.randint(3,15)
for i in range(changdu):
    suiji = random.randint(0,100)
    s.append(suiji)
print(s)
ss = max_list(s)
print(ss)
