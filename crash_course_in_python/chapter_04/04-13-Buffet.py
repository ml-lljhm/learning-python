#Learning about tuples, lists that you cant modify
foods = ('pizza', 'sushi', 'kebab', 'hamburger', 'stew')
print("This restaurant serves the following food:")
for food in foods:
    print(food.title())
foods = ('sausage', 'cat food', 'kebab', 'hamburger', 'stew')
print("The new revised menu of the restaurant is the following:")
for food in foods:
    print(food.title())
