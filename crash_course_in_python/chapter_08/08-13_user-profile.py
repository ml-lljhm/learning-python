#create user profiles using **kwargs

#the function containing **kwargs to create a dictionary with variable length
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

#setting a variable for the function call containing the arguments
user_profile = build_profile('kalle', 'anka', location='ankeborg', temperament='unstable', children='three')

#print the result of the function call
print(user_profile)
