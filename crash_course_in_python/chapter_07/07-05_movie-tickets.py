#Using a while-loop
prompt = "Enter your age to see how much a ticket would cost for you: "

age = ""

while True:
    age = input(prompt)
    age = int(age)
    
    if age < 3:
        print("Your ticket is free of charge!")
    elif age <= 12:
        print("Your ticket costs $10")
    else:
        print("Your ticket costs $15")
