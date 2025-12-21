def make_album(artist, album, tracks=None):
    formatted_dictionary = {'artist' : artist.title(), 'album' : album.title()}
    if tracks:
        formatted_dictionary['tracks'] = tracks
    
    return formatted_dictionary

print(make_album('jimi hendrix', 'are you experienced'))
print(make_album('the beatles', 'white album', tracks=30))
print(make_album('led zeppelin', 'physical graffiti', tracks=15))

