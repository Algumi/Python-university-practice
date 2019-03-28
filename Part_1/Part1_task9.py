def task_1():
    n, m = map(int, input().split())
    bor = set()
    ann = set()
    for i in range(n):
        tmp = int(input())
        ann.add(tmp)
    for i in range(m):
        tmp = int(input())
        bor.add(tmp)

    ans = bor & ann
    ann -= ans
    bor -= ans
    print(len(ans), *sorted(ans), sep='\n')
    print(len(ann), *sorted(ann), sep='\n')
    print(len(bor), *sorted(bor), sep='\n')


def task_2():
    n = int(input())
    words = set()
    for _ in range(n):
        words.update(input().split())
    print(len(words))


def task_3():
    n = int(input())
    arr = [{input() for j in range(int(input()))} for i in range(n)]
    ans1 = arr[0].intersection(*arr)
    ans2 = arr[0].union(*arr)
    print(len(ans1), *sorted(ans1), sep='\n')
    print(len(ans2), *sorted(ans2), sep='\n')



#task_1()
#task_2()
task_3()