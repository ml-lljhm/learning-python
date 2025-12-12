#Conditional tests. Just playing around with conditions to see how what will happen
motorcycle = 'hOnda'
print("Is motorcycle == 'honda'? I predict true")
print(motorcycle.lower() == 'honda')

my_age = 37
print("\nIs my age less than 40? I predict True")
print(my_age < 40 and my_age > 30)

number_of_cats = 1
print("\nDo I have less than 2 cats?")
print(number_of_cats < 2)

favorite_pizza = 'margherita'
print("\nIs my favorite pizza a vesuvio?")
if favorite_pizza == 'vesuvio':
    print("Yes")
else:
    print("No")

monies = 35
sky = 'grey'
print("\nI have at least 33 monies or the sky is blue")
if monies >= 33 or sky == 'blue':
    print("Life is good!")
else:
    print("Life is bad..")

my_drawer = ['socks']
print("\nIf my drawer contains both socks and underwear, I'm all good:")
if 'socks' in my_drawer and 'underwear' in my_drawer:
    print("My life is good indeed")
else:
    print("My life is not so good after all")

my_room = ['bedbugs', 'portal to hell']
print("\nIf my room contains neither bedbugs nor a portal to hell, I guess it's all good after all")
print(f"My life is good: {'portal to hell' not in my_room and 'bedbugs' not in my_room}")
