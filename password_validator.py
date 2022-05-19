import re

password = input()

while True:
    command = input()
    if command == "Complete":
        break
    action = command.split(" ")
    if action[0] == "Make":
        if action[1] == "Upper":
            index = int(action[2])
            symbol = password[index]
            up_symbol = symbol.upper()
            new_password = password[:index] + up_symbol + password[index + 1:]
            password = new_password
            print(password)
        elif action[1] == "Lower":
            index = int(action[2])
            symbol = password[index]
            low_symbol = symbol.lower()
            new_password = password[:index] + low_symbol + password[index + 1:]
            password = new_password
            print(password)
    elif action[0] == "Insert":
        index = int(action[1])
        char = action[2]
        if 0 <= index < len(password):
            new_password = password[:index] + char + password[index:]
            password = new_password
            print(password)
    elif action[0] == "Replace":
        char = action[1]
        value = int(action[2])
        if char in password:
            new_char = chr(ord(char) + value)
            new_password = password.replace(char, new_char)
            password = new_password
            print(password)
    elif action[0] == "Validation":
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        regex = r"[a-zA-Z0-9_]+"
        extract = re.findall(regex, password)
        check_pass = "".join(extract)
        if len(password) != len(check_pass):
            print("Password must consist only of letters, digits and _!")
        regex1 = r"[A-Z]"
        check_up = re.findall(regex1, password)
        check_pass_up = "".join(check_up)
        if not check_pass_up:
            print("Password must consist at least one uppercase letter!")
        regex2 = r"[a-z]"
        check_low = re.findall(regex2, password)
        check_pass_low = "".join(check_low)
        if not check_pass_low:
            print("Password must consist at least one lowercase letter!")
        regex3 = r"[0-9]"
        check_dig = re.findall(regex3, password)
        check_pass_dig = "".join(check_dig)
        if not check_pass_dig:
            print("Password must consist at least one digit!")
