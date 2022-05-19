heroes = dict()

while True:
    command = input().split(' ')
    if command[0] == "End":
        print("Heroes:")
        for name in heroes:
            spell_string = ", ".join(heroes[name]["spells"])
            print(f"== {name}: {spell_string}")
        break
    if command[0] == "Enroll":
        name = command[1]
        if name in heroes:
            print(f"{name} is already enrolled.")
        else:
            heroes[name] = {"spells": []}
    if command[0] == "Learn":
        name = command[1]
        spell_name = command[2]
        if name not in heroes:
            print(f"{name} doesn't exist.")
        else:
            if spell_name in heroes[name]["spells"]:
                print(f'{name} has already learnt {spell_name}')
            else:
                heroes[name]["spells"].append(spell_name)
    if command[0] == "Unlearn":
        name = command[1]
        spell_name = command[2]
        if name not in heroes:
            print(f"{name} doesn't exist.")
        else:
            if spell_name not in heroes[name]["spells"]:
                print(f"{name} doesn't know {spell_name}")
            else:
                heroes[name]["spells"].remove(spell_name)