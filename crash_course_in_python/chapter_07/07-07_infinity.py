#A loop that never ends
prompt = "Enter a number and I will double it for you: "

while True:
    number = input(prompt)
    number = int(number)
    multiply = number*2
    print(multiply)