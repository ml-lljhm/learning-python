#make a function that formats an input of a city and its country

def city_country(city, country):
    """output a formatted string of a city and its country"""
    formatted_place = f"{city.title()}, {country.title()}"
    return formatted_place
   
pair1 = city_country('kvisthån', 'sverige')
pair2 = city_country('söderhamn', 'sverige')
pair3 = city_country('husum', 'sverige')
print(f"{pair1}\n{pair2}\n{pair3}")

