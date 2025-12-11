#Playing around with dictionaries and comparing it to a list.
folks = ['will', 'mark', 'hank', 'peter', 'joey']

favorite_language = {
    'mark' : 'python',
    'matt' : 'rust',
    'jessica' : 'c++',
    'bob' : 'python',
    'hank' : 'java',
}

for folk in folks:
    if folk in favorite_language.keys():
        print(f"Thank you, {folk.title()} for participating in the poll!")
    else:
        print(f"Yo! {folk.title()}, it's time to participate in my poll!")

print(f"The coding languages present in the poll are the following: {', '.join(set(favorite_language.values()))}")