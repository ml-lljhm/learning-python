#Create three dictionaries of people
matt = {
    'first_name' : 'matt',
    'last_name' : 'baker',
    'city' : 'stockholm',
    'gender' : 'male',
}

james = {
    'first_name' : 'james',
    'last_name' : 'bond',
    'city' : 'london',
    'gender' : 'male',
}

cecilia = {
    'first_name' : 'cecilia',
    'last_name' : 'wester',
    'city' : 'göteborg',
    'gender' : 'female',
}

#Store the three dictionaries in a list
people = [matt, james, cecilia]

#Print information about the people in an organized way
for person in people:
    first = person['first_name']
    last = person['last_name']
    city = person['city']
    gender = person['gender']

    if gender == 'female':
        print(f"{first.title()} {last.title()} is a beautiful woman. She lives in {city.title()}.")
    else:
        print(f"{first.title()} {last.title()} is a man. He lives in {city.title()}.")

