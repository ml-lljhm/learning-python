#Exiting the loop with break
prompt = "Enter a topping you would like to have on your pizza: " 
prompt += "\nEnter 'quit' to exit the program.\n: " 

while True: 
    topping = input(prompt) 
    if topping != 'quit': 
        print(f"\n{topping.title()} will be added to your list of toppings.\n\n")
    else:
        break