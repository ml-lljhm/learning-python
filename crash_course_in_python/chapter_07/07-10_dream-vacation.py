#Make a script about polling people for their dream destination

#creating the prompts and setting up the dictionary and a flag
prompt = "What is your name? : "
prompt2 = "Where would your dream vacation be? : "
prompt3 = "Would another person want to answer this question? (yes/no) : "

dream_vacation = {}

active = True

#Run the poll and put the answers in the dictionary, and repeat if necessary
while active:
    name = input(prompt)
    place = input(prompt2)
    dream_vacation[name] = place
    
    repeat = input(prompt3)
    if repeat == 'no':
        active = False

#output the results from the poll
for person, destination in dream_vacation.items():
    print(f"{person.title()}'s dream destination is {destination.title()}")
