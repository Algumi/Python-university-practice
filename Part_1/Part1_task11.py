from datetime import date, timedelta


def task_1():
    d, m, y = map(int, input().split("."))
    birth_date = date(y, m, d)
    age = (date.today() - birth_date) // timedelta(days=365.2425)
    print(age)
    print(date(y + age + 1, m, d).weekday())


def task_2():
    d, m, y = map(int, input().split("."))
    life_days = int(input())
    diff = (date.today() - date(y, m, d)).days
    if diff > life_days:
        print("No")
    else:
        print("Yes", life_days - diff)

# task_1()
task_2()
