#Printing welcome messages with a special greeting for admin.
username = ['admin', 'hank', 'eric', 'grinch', 'jesus']
for user in username:
    if user == 'admin':
        print(f"Hello {user.title()}! Would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, welcome back!")
    