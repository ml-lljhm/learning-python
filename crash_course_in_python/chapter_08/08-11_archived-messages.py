#same as last task but copy the list instead of moving it

#defining the function, copy the message list and append it to another list
def send_messages(messages, sent_messages):
    """function that prints a lists and copies it to new list"""
    for current_message in messages[:]:
        sent_messages.append(current_message)
        print(f"Currently sending the message: {current_message}")


#messages and sent messages
messages = ['I am a bus driver', 'I have never been to the moon', 'What is your dogs name?', 'I like bacon and eggs']
sent_messages = []

#call upon function
send_messages(messages, sent_messages)

#verifies copy
print(f"These messages are archived: {messages}")
print(f"These messages are sent: {sent_messages}")