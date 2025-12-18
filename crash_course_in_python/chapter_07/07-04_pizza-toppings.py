#Beginning with while-loops
prompt = "Enter a topping you would like to have on your pizza: " 
prompt += "\nEnter 'quit' to exit the program.\n: " 

topping = "" 

while topping != 'quit': 
    topping = input(prompt) 
    if topping != 'quit': 
        print(f"{topping.title()} will be added to your list of toppings.\n\n")
    else:
        print("Goodbye!")