#the function containing **kwargs to create a dictionary with variable length
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
