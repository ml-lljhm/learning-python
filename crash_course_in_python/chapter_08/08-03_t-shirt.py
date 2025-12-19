#Trying out functions

#defining a function 
def shirt(size, text):
    print(f"The size of this T-shirt is: {size.upper()}")
    print(f"The text on this T-shirt is: {text}\n")

#calling the function using keyword arguments and positional arguments
shirt(text="I'm with stupid ->", size="l")
shirt("l", "I'm with stupid ->")