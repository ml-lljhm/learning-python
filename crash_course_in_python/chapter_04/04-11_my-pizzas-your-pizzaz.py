#Copying lists with slices
my_favorite_pizzas = ['margherita', 'calzone', 'tuna']
my_friends_favorite_pizzas = my_favorite_pizzas[:]
my_favorite_pizzas.append('quattro')
my_friends_favorite_pizzas.append('chicken curry')

print("My favorite pizzas are:")
for pizza in my_favorite_pizzas:
    print(pizza.title())
print("\n")

print("My friends favorite pizzas are:")
for pizza in my_friends_favorite_pizzas:
    print(pizza.title())
