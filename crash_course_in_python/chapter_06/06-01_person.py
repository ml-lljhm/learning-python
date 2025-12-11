#starting out with dictionaries
matt = {
    'first_name' : 'matt',
    'last_name' : 'baker',
    'city' : 'stockholm',
    'gender' : 'male',
}

for key, value in matt.items():
    print(f"{key}, {value}")