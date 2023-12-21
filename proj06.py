# Uncomment the following lines if you run the optional run_file tests locally
# so the input shows up in the output file. Do not copy these lines into Codio.
#
# import sys
# def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str

###############################################################################
#   Computer Project #6
#
#   Algorithm
#     Make a function called open_file to prompt the user for a file and open the file
#       if the file isnt valid make an error message appear and reprompt, this returns a file pointer
#     Make a function called read_stopwords to read the file convert all words to lowercase
#       and make a set of stopwords and close the file and return the set of stopwords
#     Make a function called validate_word to see if word in stop words or has digit or punctuation
#       this will return with either true or false
#     Make a function called process_lyrics that recives a string of lyrics and a set of stopwords
#       and strips of white space and punctuation and then checks to see if the word is valid, if it is
#       it will add that word to the set
#     Make an update_dictionary function that takes a data_dict, singer,song name, and set of song words
#       it will update the dictionary to put the new singer, song, name and lyrics in their respective places
#     Make a function called read_data this will read through the file getting the singer name, song name
#       and song lyrics and process the lyrics then update the dictionary then closes the file and returns
#       the dictionary
#     Make a function to calculate average word count which calculates avg word count by singer
#     Make a find singers vocab function that returns a dictionary of all words used by each singer
#     Make a display singers function to display the data of the singer
#     Make a function to search songs that creates a list of tuples everytime it finds a matching
#       word and sorts it alphabetically
#     Make a main function fot open the correct files, calculate all the singers data and display it
#       and also prompting the user for words to search throught the songs
#
#
###############################################################################



import csv
import string
from operator import itemgetter
PUNCTUATION = string.punctuation
DIGITS = string.digits

def open_file(message):
    ''' Prompts user to enter file with specific message
     and opens it, if file can't be opened it creates error message.'''
    y = 1
    while y > 0:
        try:
            user_file = input(message) #Promps user for file with message
            fp = open(user_file, 'r') #opens the file
            y = 0 #stops the loop
            return fp #returns file pointer
        except:
            print("\nFile is not found! Try Again!") #error message prints if file cant be opened


def read_stopwords(fp):
    ''' Gets fp of stopwords.txt, converts all stop words to lowercase and returns
    a unique set of stopwords, then closes the file'''
    stopwords_set = set() #creates empty set
    stopwords_file = fp.readlines()
    for line in stopwords_file: # goes through each line of file
        line = line.strip().lower() #strips newline and converts to lowercase
        stopwords_set.add(line) #adds word to set
    fp.close() # closes file
    return stopwords_set #returns set of stopwords

        

def validate_word(word, stopwords):
    ''' Gets a word and set of stopwords as parameters and checks to see
     if word in stop words or has digit or punctuation'''
    if word in stopwords: # checks if word is in stop words
        return False
    for ch in word: # iterates through the characters of the word
        if ch in PUNCTUATION or ch in DIGITS: #checks if character is punctuation or digits
            return False
    return True


def process_lyrics(lyrics, stopwords):
    ''' Recieves string of lyrics and a set of stopwords, it splits lyrics by a space,
    strips the whitespace then the punctuation, then validates each word using the validate function
    if word is valid it adds it to the set and returns the set of processed lyrics'''
    valid_words = set() #creates empty set
    lyrics = lyrics.replace('\n', ' ') #replaces all newline characters with spaces
    lyrics_list = lyrics.split(' ') #splits lyrics by spaces
    for i in range(len(lyrics_list)): #iterates through the list of lyrics
        lyrics_list[i] = lyrics_list[i].strip().lower() #strips each word and converts to lowercase
        check = len(lyrics_list[i]) #checks the length of the word
        if check < 1: #makes sure its not an empty space
            continue
        elif check > 1: #if its not an empty space
            lyrics_list[i] = lyrics_list[i].strip(PUNCTUATION) #strip punctuation from end
        vaild_or_not = validate_word(lyrics_list[i],stopwords) # checks if the word is valid
        if vaild_or_not == True: # if the word is valid it adds to the valid word set
            valid_words.add(lyrics_list[i])
        if '' in valid_words:
            valid_words.remove('')
    return valid_words #returns the set of valid words

def read_data(fp, stopwords):
    ''' Takes two parameters of file pointer and set of stopwords then reads in data
    collecting singer name, song name, and lyrics. It then processes the lyrics
    then updates the dictionary and closes the file and returns the dictionary'''
    data_dict = {}
    reader = csv.reader(fp)
    next(reader)
    for row in reader:
        singer = row[0]
        song = row[1]
        unprocessed_lyrics = row[2]
        lyrics = process_lyrics(unprocessed_lyrics,stopwords)
        update_dictionary(data_dict,singer,song,lyrics)
    fp.close()
    return data_dict

def update_dictionary(data_dict, singer, song, words):
    '''Takes data_dict, a singer, a song, and a set of song words and places the new song
    and song words key values pairs in the right dictionary under the specified singer'''
    song_dict = {} #creates empty dictionary
    if data_dict.get(singer) != None: #checks to see if it is already in main dictionary
        song_dict[song] = words #creats dictionary of song and lyrics
        data_dict[singer].update(song_dict) #if so adds the song and lyrics to inner dicionary
    else:
        song_dict[song] = words #creates song dictionary with song and the lyrics
        data_dict[singer] = song_dict #adds that dictionary to the singer
    return None
        
def calculate_average_word_count(data_dict):
    ''' receives data_dict and calculates avg word count for singer and returns another
    dictionary of all the singers and their average word count'''
    avg_word_dict = {}
    count = 0
    for key,value in data_dict.items():
        length = len(value)
        singer = key
        for n in value.values():
            count += len(n)
        avg_words = count / length
        avg_word_dict[singer] = avg_words
        count = 0
    return avg_word_dict

def find_singers_vocab(data_dict):
    '''receives data_dict and creates a union of all the words that are used by the singer
    and then creates a dictionary to store the singer and the singers vocab'''
    singer_vocab = {}
    list_of_sets = []
    for key, value in data_dict.items():
        singer = key
        length = len(value)
        for n in value.values():
            list_of_sets.append(n)
        #for i in range(len(list_of_sets) - 1):
            #vocab_set = list_of_sets[i] | list_of_sets[i + 1]
        vocab_set = set.union(*list_of_sets)
        singer_vocab[singer] = vocab_set
        list_of_sets = []
    return singer_vocab

def display_singers(combined_list):
    ''' Gets a list of tuples from main program sorts that list by avg word count and then vocab size
    and then displays the top 10 results'''
    sorted_results = sorted(combined_list, key=itemgetter(1,3),reverse=True)
    print("\n{:^80s}".format("Singers by Average Word Count (TOP - 10)"))
    print("{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer","Average Word Count", "Vocabulary Size", "Number of Songs"))
    print('-' * 80)
    count = 0
    for n in sorted_results:
        if count < 10:
            print("{:<20s}{:>20.2f}{:>20d}{:>20d}".format(n[0], n[1], n[3], n[2]))
            count += 1

    "\n{:^80s}".format("Singers by Average Word Count (TOP - 10)")
    "{:<20s}{:>20s}{:>20s}{:>20s}".format("Singer","Average Word Count", "Vocabulary Size", "Number of Songs")
    '-' * 80

    return None


def search_songs(data_dict, words):
    ''' gets data_dict and a set of words it creates a list of tuples everytime it finds a match'''
    list_of_songs = []
    for key, value in data_dict.items():
        for song, lyrics in value.items():
            if words.issubset(lyrics):
                list_of_songs.append(tuple((key, song)))
    sorted_list = sorted(list_of_songs, key=itemgetter(0,1))
    return sorted_list

def main():
    stopwords_fp = open_file('\nEnter a filename for the stopwords: ')
    song_data_fp = open_file('\nEnter a filename for the song data: ')
    stopwords = read_stopwords(stopwords_fp)
    song_data = read_data(song_data_fp,stopwords)
    avg_word_count_dict = calculate_average_word_count(song_data)
    singers_vocab_dict = find_singers_vocab(song_data)
    list_of_data = []
    for singer, songs in song_data.items():
        length = len(songs)
        avg_word_sing = avg_word_count_dict[singer]
        singer_vocab = len(singers_vocab_dict[singer])
        singer_data = tuple((singer,avg_word_sing,length,singer_vocab))
        list_of_data.append(singer_data)
    display_singers(list_of_data)
    print("\nSearch Lyrics by Words")
    y = 1
    while y > 0:
        words = input("\nInput a set of words (space separated), press enter to exit: ")
        words = words.lower()
        if words == '':
            y = 0
            continue
        words = words.split(" ")
        words = set(words)
        amount = 0
        for i in words:
            if validate_word(i,stopwords) == True:
                amount += 1

        if amount != len(words):
            print('\nError in words!')
            print('\n1-) Words should not have any digit or punctuation')
            print('\n2-) Word list should not include any stop-word')
            continue


        found_songs = search_songs(song_data,words)
        amount_songs = len(found_songs)
        if amount_songs == 0:
            print("\nThere are {} songs containing the given words!".format(amount_songs))
        else:
            print("\nThere are {} songs containing the given words!".format(amount_songs))
            print("{:<20s} {:<s}".format('Singer','Song'))
        count = 0
        for song in found_songs:
            if count < 5:
                print("{:<20s} {:<s}".format(song[0],song[1]))
                count += 1

    '\nEnter a filename for the stopwords: '
    '\nEnter a filename for the song data: '
    "\nSearch Lyrics by Words"


    "\nInput a set of words (space separated), press enter to exit: "
    '\nError in words!'
    "\nThere are {} songs containing the given words!"
    "{:<20s} {:<s}"
    pass
if __name__ == '__main__':
    main()           
