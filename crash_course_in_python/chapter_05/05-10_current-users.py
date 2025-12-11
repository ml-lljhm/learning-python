#Comparing new_users to current_users to see there are no duplicates
new_users = ['matt', 'marcus', 'eric', 'jeSus', 'geoRge']
current_users = ['banana', 'paul', 'john', 'jesus', 'george']

#making a new list with lower-case
new_users_lower = [x.lower() for x in new_users]

#check whether the username is taken or not
for user in new_users_lower:
    if user in current_users:
        print(f"Sorry the username '{user}' is already taken, please choose a new one.")
    else:
        print(f"The username '{user}' is available.")


