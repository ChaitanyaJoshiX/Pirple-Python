"""
Creating a dictionary of my favourite song.
Printing out each key and it's value through a loop.
Also, creating a function that allows the user to guess the value of any key .
If the key exists in dictionary and the value is correct, function returns true.
Or else, it returns false.
"""
#Base program starts here
SongDetails = {"Artist":"OneRepublic", "Genre":"Pop", "Duration":169,
               "YearofRelease":2021, "LikeDislikeRatio":95.18, "Views":6410185,
               "Album":"Human", "LeadVocalist":"Ryan Tedder"}
print("Key\t\tValue")
for detail in SongDetails:
    print(detail +"\t\t"+ (str(SongDetails[detail])))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
"""
Identation will vary as per terminal display settings
"""
#Extra credit stars here
def Guess(key, value):
    c = 0
    for detail in SongDetails:
        SongDetails[detail] == str(SongDetails[detail])
        if key == detail and value == SongDetails[detail]:
            return True
            c += 1
    if c !=1:
        return False
#Testing out the function from here
#Tried using input with my current knowledge but failed so hardcoded the checks
print(Guess("YearofRelease", 2021)) #Will return True
print(Guess("LikeDislikeRatio", 65.6)) #Will return False
print(Guess("HitorFlop", "Hit")) #Will return False
