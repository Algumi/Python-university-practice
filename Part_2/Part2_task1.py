import math


def task_1_1(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


def task_1_2(a, b, c):
    m = max(a, b, c)
    return m < a + b + c - m


def task_1_3(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p-a) * (p-b) * (p-c))


def task_1():
    arr = list(map(int, input().split()))
    min_sqr = float("inf")
    ans = []
    for x, y in zip(arr[0::2], arr[1::2]):
        for x1, y1 in zip(arr[0::2], arr[1::2]):
            for x2, y2 in zip(arr[0::2], arr[1::2]):
                a, b, c = [task_1_1(x, y, x1, y1), task_1_1(x1, y1, x2, y2), task_1_1(x2, y2, x, y)]
                if task_1_2(a, b, c):
                    t_sqr = task_1_3(a, b, c)
                    if t_sqr != 0 and t_sqr < min_sqr:
                        min_sqr = t_sqr
                        ans = [(x, y), (x1, y1), (x2, y2)]
    print(*ans, round(min_sqr, 1))


def change(a, b):
    c = a.copy()
    del a[:]
    a.extend(b)
    del b[:]
    b.extend(c)


def task_3():
    f = open('test_data/Test_data_part2_task1_3.txt', 'r')
    c = f.read(2)[0]
    ans = (0, 0)
    i = 0
    for line in f:
        s = "".join((filter(str.isalpha, line)))
        pers = s.count(c) / max(len(s), 1)
        if pers > ans[0]:
            ans = (pers, i)
        i += 1
    print(round(ans[0] * 100), ans[1])


def task_4():
    inp = input()
    cur_items = []
    cur_sum = 0
    check_num = 1
    while inp != "#":
        if inp[:8] == "add_item":
            item, cost = inp[10:-1].split("', ")
            cur_items.append((item, cost))
            cur_sum += int(cost)
        if inp[:8] == "print_re" and cur_items:
            print("Чек %d. Всего предметов: %d" % (check_num, len(cur_items)))
            for item in cur_items:
                print(item[0], "-", item[1])
            print("Итого:", cur_sum, "\n-----")
            check_num += 1
            cur_items = []
            cur_sum = 0
        inp = input()


def test_task2():
    a = [1, 2, 3, 9, 11]
    b = [7, 9, 8]
    print("Before:", a, b)
    change(a, b)
    print("After", a, b)


# 0 0 5 5 0 1 1 0
#task_1()

test_task2()
# task_3()
# task_4()



