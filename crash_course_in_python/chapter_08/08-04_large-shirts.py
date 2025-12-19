#Trying out functions

#defining a function with default values
def shirt(size='L', text='I love python'):
    print(f"The size of this T-shirt is: {size.upper()}")
    print(f"The text on this T-shirt is: {text}\n")

#calling the function using keyword arguments and positional arguments, with and without default values
shirt()
shirt(size='M')
shirt(text="I'm with stupid ->")
