#converting string to integer and comparing numbers
seating = input("How many people are in your dinner group? Please enter here: ")
seating = int(seating)

if seating >= 8:
    print("I'm sorry, you will have to wait for a table.")
else:
    print("There is a table available for you!")