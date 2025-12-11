#Using dictionaries and retrieving certain parts from it
rivers = {
    'nile' : 'egypt',
    'ganges' : 'india',
    'götakanal' : 'sweden'
}

for river, country in rivers.items():
    print(f"The river {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.title())