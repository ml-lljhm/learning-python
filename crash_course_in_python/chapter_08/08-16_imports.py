#playing around with importing functions

from profile_function import *

#setting a variable for the function call containing the arguments
user_profile = build_profile(
    'kalle',
    'anka', 
    location='ankeborg', 
    temperament='unstable', 
    children='three'
)

#print the result of the function call
print(user_profile)
