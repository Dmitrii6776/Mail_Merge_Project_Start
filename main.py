with open("./Input/Names/invited_names.txt") as names:
    names_list = names.read()
    names_list = names_list.split('\n')
    print(names_list)
with open("./Input/Letters/starting_letter.txt") as l:
    letter = l.read()
    for name in names_list:
        print(name)
        letter_to_send = letter.replace('[name]', f"{name}")

        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as ls:
            ls.write(f'{letter_to_send}')







