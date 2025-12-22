#creating a function that prints and moves messages from one list to another

def send_messages(messages, sent_messages):
    """printing out the contents of a list and moving it to a new list"""
    while messages:
        current_message = messages.pop()
        print(f"Moving this message: {current_message}")
        sent_messages.append(current_message)



#lists of messages to send and sent messages
messages = ['Hello my name is Greger!', 'I should probably write some messages..', 'Or this script wont make sense!']
sent_messages = []

#call upon the function with both lists
send_messages(messages, sent_messages)

#verify that the function have moved the messages between the lists
print(f"These messages are left to be sent: {messages}")
print(f"These messages have been sent: {sent_messages}")
