def task_1():
    n = int(input())
    arr = [['.'] * n for i in range(n)]
    for i in range(n):
        arr[i][i] = '*'
        arr[n // 2][i] = '*'
        arr[i][n // 2] = '*'
        arr[i][n - i - 1] = "*"

    for i in arr:
        print(*i)


def task_2():
    n = int(input())
    arr = [['.'] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            arr[i][j] = abs(j - i)

    for i in arr:
        print(*i)


def task_3():
    n = int(input())
    arr = [input() for i in range(n)]
    ans = '-'
    for s in arr:
        if "xxx" in s:
            ans = "x"
        elif "ooo" in s:
            ans = "o"

    for i in range(n):
        tmp = ""
        for s in arr:
            tmp += s[i]
        if "xxx" in s:
            ans = "x"
        elif "ooo" in s:
            ans = "o"

    print(ans)


#task_1()
#task_2()
task_3()