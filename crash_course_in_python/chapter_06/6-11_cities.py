#Making nested dictionaries containing cities and information about them
cities = {
    'vemhån' : {'population' : 200, 'country' : 'sweden', 'info' : 'Its a nice village'},
    'kvisthån' : {'population' : 3, 'country' : 'sweden', 'info' : 'It might not even exist anymore'},
    'vemdalen' : {'population' : 1000, 'country' : 'sweden', 'info' : 'Its great for skiing'}
}

#Printing it out in an organized way
for name, facts in cities.items():
    population = facts['population']
    country = facts['country']
    info = facts['info']
    print(f"\n{name.title()} is a nice village! It resides in {country.title()} and has a population of {population:,} people."
          f" Fun fact: {info}.")
    