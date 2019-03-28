def task_1(s):
    print(s[2])
    print(s[-2])
    print(s[:5])
    print(s[:-2])
    print(s[::2])
    print(s[1::2])
    print(s[::-1])
    print(s[::-2])
    print(len(s))
    
def task_2(s):
    first = s.find("f")
    last = s.rfind("f")
    if first == -1:
        return
    elif first == last:
        print(first)
    else:
        print(first, last)

def task_3(s):
    first = s.find("h")
    last = s.rfind("h") - 1
    print(s[last:first:-1])
    
def task_4(s):
    first = s.find("h") + 1
    last = s.rfind("h") - 1
    print(s[:first] + s[first:last].replace("h", "H") + s[last:])

def task_5(s):
    print(s.replace("@", ""))


# test data - rainbow_test
# test  letfbethere  trefkorpcefght
# testdatahprinteddatahendtest
# testhtesthtesthttphtesthtest
# test@delete@*(&%(^(&)))@
def test():
    s = input()
    task_3(s)

test()