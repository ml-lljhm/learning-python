#Same as last exercise, but check and remove pastrami sandwiches
sandwich_orders = ['tuna sandwish', 'curry chicken', 'meatball sandwich', 'pastrami', 'ham and cheese', 'pastrami', 'pastrami']
finished_sandwiches = []

#checks if there is pastrami sandwiches in the order
if 'pastrami' in sandwich_orders:
    print("Sorry we have run out of pastrami sandwiches!")

#if there are pastrami sandwiches, remove them
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
#switch sandwiches from one list to the other
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"Currently making your {current_sandwich.title()}.")

print("\nThe following sandwiches are now ready:\n")
for sandwiches in finished_sandwiches:
    print(f"{sandwiches.title()}")