# section 1
def first_task():
    n = int(input())
    print ((n // 60) % 24)
    print (n % 60)

def second_task():
    a, b, c = map(int, input().split())
    print ((a+1) // 2 + (b+1) // 2 + (c+1) // 2)
    
def third_task():
    a, b, l, N = map(int, input().split())
    print (2 * (N * (a+b) + l - b) - a)

#first_task()
#second_task()
#third_task()
    

    
