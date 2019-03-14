def task_1():
    n, words = int(input()), dict()
    for i in range(n):
        for x in input().split():
            words[x] = words.get(x, 0) + 1

    for i in range(max(words.values()), 0, -1):
        for k in sorted(x for x in words if words[x] == i):
            print(k)


def task_2():
    n, tree, heights = int(input()), dict(), dict()
    for _ in range(n - 1):
        child, parent = input().split()
        tree[child] = parent
        heights[parent] = 0

    for _ in range(len(tree)):
        for person in tree.keys():
            heights[person] = heights[tree[person]] + 1

    for key, value in sorted(heights.items()):
        print(key, value)


def task_3():
    data = dict()
    for _ in range(int(input())):
        name, day, month = input().split()
        if month in data.keys():
            data[month].append((int(day), name))
        else:
            data[month] = [(int(day), name)]
    for _ in range(int(input())):
        month = input()
        if month in data.keys():
            print(*((i[1] + " " + str(i[0]) for i in sorted(data[month]))))

#task_1()
#task_2()
task_3()