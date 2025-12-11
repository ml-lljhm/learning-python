#Using the dictionary-function as a glossary
glossary = {
    'print()' : 'prints an output to the scren',
    '.get()' : 'retrieves an item from a dictionary',
    '.items()' : 'retrieves both the key and value from a dictionary',
    '.keys()' : 'retrieves the key of a key:value-pair from a dictionary',
    '.values()' : 'retrieves the value of a key:value-pair from a dictionary',
}

for command, explanation in glossary.items():
    print(f'The command "{command}" does this:')
    print(f"{explanation.capitalize()}\n")