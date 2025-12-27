#functions other scripts can import

#function that removes items from one list and moves it to another list
def print_models(unprinted_designs, completed_models):
    """
    print each design until none is left
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Currently printing model: {current_design.title()}")
        completed_models.append(current_design)

#show that items have been moved between lists
def show_completed_models(completed_models):
    """
    show the completed models
    """
    print("\nThe current models have been completed:\n")
    for completed_model in completed_models:
        print(f"- {completed_model.title()}")
        