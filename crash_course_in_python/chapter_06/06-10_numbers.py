#Store one to two favorite numbers
favorite_numbers = {
    'matt' : ['13', '5'],
    'josh' : ['21', '9'],
    'trey' : '6',
    'markus' : ['333', '9'],
    'jonas' : '1',
}

#Use if/else function to make a prettier output
for name, numbers in favorite_numbers.items():
    if isinstance(numbers, list):
        formatted_numbers = ' and '.join(numbers)
        print (f"{name.title()}'s favorite numbers are: {formatted_numbers}.")
    else:
        print(f"{name.title()}'s favorite number is {numbers}.")