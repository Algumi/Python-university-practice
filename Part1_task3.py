def task_1(n):
    ans = 540 + n * 50 - 5
    if n > 6:
        ans += 30
    elif n > 4:
        ans += 20
    elif n > 2:
        ans += 10
    print(ans // 60, ans % 60)

def task_2(h, m, s):
    h_degr = 360 / 12
    m_degr = h_degr / 60
    s_degr = h_degr / 60
    print(h_degr * h + m_degr * m + s_degr * s)

def task_3(a):
    print(a % 30 * 12)

def task_4(p, x, y):
    ans = (x * 100 + y) * (1 + p / 100)
    print(int(ans // 100), int(ans % 100))

def test_task_1():
    n = int(input())
    task_1(n)

def test_task_2():
    h, m, s = map(int, input().split())
    task_2(h, m, s)

def test_task_3():
    a = float(input())
    task_3(a)

def test_task_4():
    p, x, y = map(int, input().split())
    task_4(p, x, y)

#test_task_1()
test_task_2()
#test_task_3()
#test_task_4()