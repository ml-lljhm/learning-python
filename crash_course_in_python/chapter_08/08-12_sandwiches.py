#Create a function using *args

#print the sandwich orders
def sandwiches(*toppings):
    """prints the toppings for a given sandwich using *args"""
    print(f"\nThe sandwich will have the following toppings:")
    for topping in toppings:
        print(topping.title())

#the orders themselves
sandwiches('cheese', 'ham', 'tomato')
sandwiches('egg', 'bacon', 'cat litter', 'salad')
sandwiches('olive oil', 'salt')