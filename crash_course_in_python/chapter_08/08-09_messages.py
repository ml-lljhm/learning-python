#Practicing calling upon functions

def show_messages(messages):
    """printing out the contents of a list"""
    for message in messages:
        print(f'A message from the list: {message}\n')

messages = ['Hello my name is Greger!', 'I should probably write some messages..', 'Or this script wont make sense!']
show_messages(messages)