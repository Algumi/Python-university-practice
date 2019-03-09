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
    
task_1()
