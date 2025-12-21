#the function for creating dictionaries of albms
def make_album(artist, album, tracks=None):
    """a function that creates a dictionary of artist, album and an optional key/value pair for track number"""
    formatted_dictionary = {'artist' : artist.title(), 'album' : album.title()}
    if tracks:
        formatted_dictionary['tracks'] = tracks
    
    return formatted_dictionary

#defining the prompts
prompt1 = "\nEnter a band you like: "
prompt2 = "\nEnter an album by the band: "
prompt3 = "\nOptionally enter how many tracks is on the album. (if not, just hit enter): "
prompt4 = "\nWould you like to enter a new artist? (yes/no)"


while True:
    artist = input(prompt1)
    album = input(prompt2)
    tracks = input(prompt3)
    
    print(make_album(artist, album, tracks))
    
    new_band = input(prompt4)
    if new_band == 'no':
        break

