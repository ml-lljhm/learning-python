#Make three dictionaries of pets and some information of them. Store them in a list and print it out in an organized way

#Three dictionaries
klöver = {
    'animal' : 'cat',
    'name' : 'klöver',
    'age' : 4,
    'owner' : 'cecilia',
}

siri = {
    'animal' : 'cat',
    'name' : 'siri',
    'age' : 9,
    'owner' : 'emil',
}

ronja = {
    'animal' : 'dog',
    'name' : 'ronja',
    'age' : 5,
    'owner' : 'claes',
}

#Make the dictionaries into a list
pets = [klöver, siri, ronja]

#Print the pets out with information about them
for pet in pets:
    animal = pet['animal']
    name = pet['name']
    age = pet['age']
    owner = pet['owner']

    print(f"{name.title()} is a {animal} that is {age} years old. Its owners name is {owner.title()}.")