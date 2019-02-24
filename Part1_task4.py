def task_1(a, b):
    for i in range(a - (1 - a % 2), b - 1, -2):
        print(i)

def task_2():
    n = int(input())
    ans = 0
    for i in range(n):
        if int(input()) == 0:
            ans += 1
    print(ans)
    
def task_3():
    n = int(input())
    ans = n
    for i in range(1, n):
        ans += i
        ans -= int(input())
    print(ans)
        

def test_1():
    a, b = map(int, input().split())
    task_1(a, b)

test_1()
#task_2()
#task_3()