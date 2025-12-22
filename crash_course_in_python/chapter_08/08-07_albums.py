#the function for creating dictionaries of albms
def make_album(artist, album, tracks=None):
    """a function that creates a dictionary of artist, album and an optional key/value pair for track number"""
    formatted_dictionary = {'artist' : artist.title(), 'album' : album.title()}
    if tracks:
        formatted_dictionary['tracks'] = tracks
    
    return formatted_dictionary

#the values for the dictionaries
print(make_album('jimi hendrix', 'are you experienced'))
print(make_album('the beatles', 'white album', tracks=30))
print(make_album('led zeppelin', 'physical graffiti', tracks=15))

