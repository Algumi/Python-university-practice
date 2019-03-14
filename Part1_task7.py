def task_1():
    arr = list(map(int, input().split()))
    
    print("part 1:", end = " ")
    ans = True
    prev = 0
    part_2_ans = ()
    for i in arr:
        if i % 2 == 0:
            print(i, end = " ")
            
        if ans and prev * i > 0:
            part_2_ans = (prev, i)
            ans = False
        prev = i
    
    print("\npart 2:", *part_2_ans)
    
    print("part 3:\nmin, max:", min(arr), max(arr))
    print("indexes:", arr.index(min(arr)), arr.index(max(arr)))
    
    arr.sort()
    ans_4 = 0
    prev = "0"
    for i in arr:
        if i != prev:
            ans_4 += 1
        prev = i
    print("part 4:", ans_4)
    
    
def task_2():
    arr = list(map(int, input().split()))
    
    arr_x = arr_y = diag_l = diag_r = []
    ans = True
    for i in range(0, len(arr), 2):
        x = arr[i]
        y = arr[i + 1]
        d_l = x / y
        d_r = y / x
        
        check = arr_x.count(x) + arr_y.count(y) + diag_l.count(d_l) + diag_r.count(d_r)
        if (check > 0):
            ans = False
        
        arr_x.append(x)
        arr_y.append(y)
        diag_l.append(d_l)
        diag_r.append(d_r)
    if ans:
        print("NO")
    else:
        print("YES")
    
def task_3():
    arr = list(input().split(","))
    
    for s in arr:
        ans = True
        for i in s:
            if not (i.isalpha() or i.isdigit() or i == "_"):
                ans = False
        if not ans:
            print(s)

import math
def task_4():
    data = list(input().split(" "))
    
    nums = []
    for s in data:
        if s[0].isdigit():
            nums.append(int(s))
        else:
            if s == "*":
                a = nums.pop()
                b = nums.pop()
                nums.append(a * b)
            elif s == "-":
                a = nums.pop()
                b = nums.pop()
                nums.append(b - a)
            elif s == "+":
                a = nums.pop()
                b = nums.pop()
                nums.append(a + b)
            elif s == "/":
                a = nums.pop()
                b = nums.pop()
                nums.append(b // a)
            elif s == "~":
                a = nums.pop()
                nums.append(-a)
            elif s == "!":
                a = nums.pop()
                nums.append(math.factorial(a))
            elif s == "#":
                a = nums.pop()
                nums.append(a)
                nums.append(a)
            elif s == "@":
                a = nums.pop()
                b = nums.pop()
                c = nums.pop()
                nums.append(b)
                nums.append(a)
                nums.append(c)
    print(nums.pop())


#task_1()
#task_2()
#task_3()
task_4()