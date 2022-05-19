import re

n = int(input())

for i in range(n):
    password = input()
    regex = r'^(.+)>(?P<password>[0-9]{3}\|[a-z]{3}\|[A-Z]{3}\|[^(\<|\>)]+)<\1'
    extract = re.finditer(regex, password)
    pass_list = []
    for item in extract:
        pass_list.append(item.group("password"))
    if pass_list:
        pass_word = ''.join(pass_list)
        encrypted = pass_word.replace("|", '')
        print(f"Password: {encrypted}")
    else:
        print("Try another password!")