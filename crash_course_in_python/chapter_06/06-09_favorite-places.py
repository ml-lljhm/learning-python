#Defining some favorite places for people
favorite_places = {
    'cecilia' : ['venice', 'paris', 'liverpool'],
    'batman' : 'gotham city',
    'cartman' : ['south park', 'new york'],
}

#Structuring the output into 
for name, place in favorite_places.items():
    if isinstance(place, list):
        formatted_places = ', '.join(place)
        print(f"{name.title()} has {len(place)} favorite places which are the following: {formatted_places.title()}")
    else:
        print(f"{name.title()}'s favorite place is {place.title()}")

