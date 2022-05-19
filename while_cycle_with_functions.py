def add(lst, value):
    lst.append(value)


def remove(lst, value):
    if value in lst:
        lst.remove(value)


def replace(lst, value, new_value):
    if value in lst:
        index = lst.index(value)
        new_str = [new_value]
        new_lst = lst[:index] + new_str + lst[index + 1:]
        lst.clear()
        for i in new_lst:
            lst.append(i)


def collapse(lst, value):
    temp = lst.copy()
    for i in lst:
        if int(i) < int(value):
            temp.remove(i)
    lst.clear()
    for i in temp:
        lst.append(i)


nums = [x for x in input().split(" ")]

while True:
    command = input().split(' ')
    if command[0] == "Finish":
        print(" ".join(nums))
        break
    elif command[0] == "Add":
        add(nums, command[1])
    elif command[0] == "Remove":
        remove(nums, command[1])
    elif command[0] == "Replace":
        replace(nums, command[1], command[2])
    elif command[0] == "Collapse":
        collapse(nums, command[1])
