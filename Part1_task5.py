def task_1():
    tmp = 1
    max_2 = 0
    max_1 = 0
    while tmp != 0:
        tmp = int(input())
        if max_1 < tmp:
            max_2 = max_1
            max_1 = tmp
        elif max_2 < tmp:
            max_2 = tmp
    print(max_2)
    
def task_2():
    cur_num = 1
    last = 0
    ans = 0
    tmp = 1
    while tmp != 0:
        tmp = int(input())
        if tmp == last:
            cur_num += 1
        else:
            cur_num = 1
        if ans < cur_num:
                ans = cur_num
        last = tmp
    print(ans)
    
from math import sqrt

def task_3():
    tmp = 1
    sum_1 = 0
    sum_2 = 0
    n = -1
    while tmp != 0:
        tmp = int(input())
        n += 1
        sum_1 += tmp
        sum_2 += tmp * tmp
    print(sqrt(sum_2  - sum_1 * sum_1 / n) / (n - 1))


task_1()
#task_2()
#task_3()
        