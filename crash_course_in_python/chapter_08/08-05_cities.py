#Defining a function with a default value
def describe_city(city, country='north korea'):
    print(f"{city.title()} is a city in {country.title()}.\n")

#toying around with the default value
describe_city('pyongyang')
describe_city('liverpool', country='england')
describe_city('norrköping', country='sweden')