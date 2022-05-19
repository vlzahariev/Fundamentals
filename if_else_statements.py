import math
budget = float(input())
students = int(input())
pack_flour = float(input())
one_egg = float(input())
apron = float(input())

free_flour = 0
if students >= 5:
    free_flour = students // 5

spent = apron * math.ceil(students * 1.2) + one_egg * 10 * students + pack_flour * (students - free_flour)

diff = abs(budget - spent)

if budget >= spent:
    print(f'Items purchased for {spent:.2f}$.')
else:
    print(f'{diff:.2f}$ more needed.')
