def add(lst, value):
    if value in lst:
        print("Card is already in the deck")
    else:
        lst.append(value)
        print("Card successfully added")


def remove(lst, value):
    if value not in lst:
        print("Card not found")
    else:
        lst.remove(value)
        print("Card successfully removed")


def remove_at(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
        print('Card successfully removed')
    else:
        print('Index out of range')


def insert(lst, index, value):
    if 0 <= index < len(lst):
        if value in lst:
            print("Card is already added")
        else:
            lst.insert(index, value)
            print("Card successfully added")
    else:
        print('Index out of range')


cards = [x for x in input().split(', ')]
n = int(input())

for i in range(n):
    command = input().split(', ')
    if command[0] == "Add":
        add(cards, command[1])
    if command[0] == "Remove":
        remove(cards, command[1])
    if command[0] == "Remove At":
        remove_at(cards, int(command[1]))
    if command[0] == "Insert":
        insert(cards, int(command[1]), command[2])

print(', '.join(cards))
