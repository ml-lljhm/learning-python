#Printing welcome messages with a special greeting for admin.
#Also checking if there is any users at all.
username = []

if username:
    for user in username:
        if user == 'admin':
            print(f"Hello {user.title()}! Would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, welcome back!")
else:
    print("We need to add more users!")