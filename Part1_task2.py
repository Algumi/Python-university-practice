def task_1(x_a, y_a, x_b, y_b):
    if (x_a + y_a) % 2 == (x_b + y_b) % 2:
        print("YES")
    else:
        print("NO")


def task_2(x_a, y_a, x_b, y_b):
    if abs(x_a - x_b) < 2 and abs(y_a - y_b) < 2:
        print("YES")
    else:
        print("NO")

def task_3(x_a, y_a, x_b, y_b):
    if abs(x_a - x_b) == abs(y_a - y_b) or x_a == x_b or y_a == y_b:
        print("YES")
    else:
        print("NO")

def task_4(x_a, y_a, x_b, y_b):
    if abs(x_a - x_b) == 1 and abs(y_a - y_b) == 2:
        print("YES")
    elif abs(x_a - x_b) == 2 and abs(y_a - y_b) == 1:
        print("YES")
    else:
        print("NO")

def task_5(N, M, x, y):
    if N > M:
        N, M = M, N
    if min(x, N - x) < min(y, M - y):
        print(min(x, N - x))
    else:
        print(min(y, M - y))


def test_task():
    a, b, c, d = map(int, input().split())
    task_5(a, b, c, d)

test_task()
