#just a script to practice using **kwargs with

#defining function using **kwargs and having manufacturer and model be mandatory. 
def car_format(manufacturer, model, **information):
    """function for creating a dictionary of car information"""
    information['manufacturer'] = manufacturer
    information['model'] = model
    return information

#assign the function call to a variable
car_information = car_format('Volvo', 'V70', color='Blue', boring=True, sturdy='yes')

#print result
print(car_information)
