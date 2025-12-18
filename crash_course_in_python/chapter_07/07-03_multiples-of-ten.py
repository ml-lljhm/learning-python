#Using the modulo operator to see if a given number is a multiple of ten
number = input("Give me a number and I will tell you if it is a multiple of ten or not: ")
number = int(number)

if number % 10 == 0:
    print("The number is a multiple of ten.")
else:
    print("The number is not a multiple of ten.")
