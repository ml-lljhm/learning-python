#Taking sandwich orders and finishing them using a while loop
sandwich_orders = ['tuna sandwish', 'curry chicken', 'meatball sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"Currently making your {current_sandwich.title()}.")

print("\nThe following sandwiches are now ready:\n")
for sandwiches in finished_sandwiches:
    print(f"{sandwiches.title()}")