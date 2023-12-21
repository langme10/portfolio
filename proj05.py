# Uncomment the following lines if you run the optional run_file tests locally
# so the input shows up in the output file. Do not copy these lines into Codio.
#
#import sys
#def input( prompt=None ):
      #if prompt != None:
        #print( prompt, end="" )
    #aaa_str = sys.stdin.readline()
    #aaa_str = aaa_str.rstrip( "\n" )
    #print( aaa_str )
    #return aaa_str


###############################################################################
#   Computer Project #5
#
#   Algorithm
#     Make a function called open_file to open the file
#     Make a function called read_file to read the file and make list of lists
#     Make a function called num_in_common_between_lists to find num in common
#       between two lists
#     Make a function called calc_similarity_scores to calculate a matrix with teh similarity scores
#     Make a function called recommend to recommend the new friend
#     Make a main function for user inputs and running the loop for the program
#
###############################################################################

def open_file():
    ''' Prompts user for input and tries to open the data file if file name
    is invalid it creates and error and keeps looping for input'''
    y = 1
    while y > 0:
        user_file =  input("\nEnter a filename: ")
        try:
            fp = open(user_file, 'r')
            y = 0
        except:
            print("\nError in filename.")
    return fp


def read_file(fp):
    ''' take in a file pointer then reads the file making a list with n lists inside of it
    n is the number of user gotten from the first line, it then reads each line and places the
    friends in each respective list in the network list'''
    network_list = [] # empty list that with get n lists inside it
    count = 0
    n = 0
    for line in fp: # gets number of users from first line
        if count == 0:
            n = int(line)
            count += 1
        break
    for i in range(n): # appends n number of lists inside network list
        network_list.append([])

    for line in fp: #gets the numbers from each line and appends them to the respective lists
        line_list = line.split(' ')
        line_list[0] = int(line_list[0])
        line_list[1] = int(line_list[1])
        network_list[line_list[0]].append(line_list[1])
        network_list[line_list[1]].append(line_list[0])

    return network_list

def num_in_common_between_lists(list1, list2):
    ''' takes in two lists and sees how many friends they have in common and return that in
    integer form'''
    count = 0
    if len(list1) > len(list2): #sees if list1 is bigger than list 2
        for i in list1: # loops through each list and sees if they have similaritie, if so count increases
            for n in range(len(list2)):
                if i == list2[n]:
                    count += 1
    else:
        for i in list2:
            for n in range(len(list1)):
                if i == list1[n]:
                    count += 1

    return count

def calc_similarity_scores(network):
    ''' Takes the network as a parameter then makes a similarity matrix for all users'''
    network_count = len(network) # gets network count
    similarity_matrix = []
    for i in range(len(network)): # makes similarity matrix
        new_list = []
        similarity_matrix.append(new_list)

    for i in range(len(network)):
        for n in range(len(network)):
            score = num_in_common_between_lists(network[i],network[n])
            similarity_matrix[i].append(score)

    return similarity_matrix


def recommend(user_id, network, similarity_matrix):
    ''' takes in user Id, similarity matrix, and network and finds the recommended friend
    for the chosen user id'''
    highest = 0
    num = 0
    for count, char in enumerate(similarity_matrix[user_id]):
        if count == user_id:
            continue
        elif count in network[user_id]:
            continue
        elif char > highest:
            highest = char
            num = count
        elif char == highest:
            if count < highest:
                num = count

    return num


def main():
    # by convention "main" doesn't need a docstring
    print("Facebook friend recommendation.\n")
    file_pointer = open_file()
    network = read_file(file_pointer)
    similarity = calc_similarity_scores(network)
    z = 1
    while z > 0:
        try:
            user_id = int(input("\nEnter an integer in the range 0 to {}:".format(len(network)-1)))
            if user_id < 0:
                print("\nError: input must be an int between 0 and {}".format(len(network)-1))
                continue
            elif user_id > len(network)-1:
                print("\nError: input must be an int between 0 and {}".format(len(network) - 1))
                continue
            recommended_user = recommend(user_id,network,similarity)
            print("\nThe suggested friend for {} is {}".format(user_id,recommended_user))
            proceed_program = input("\nDo you want to continue (yes/no)? ").lower()
            if proceed_program == 'no':
                z = 0

        except:
            print("\nError: input must be an int between 0 and {}".format(len(network)-1))

    "\nDo you want to continue (yes/no)? "
    "\nEnter a filename: "
    "\nError in filename."
    "\nThe suggested friend for {} is {}"
    "\nEnter an integer in the range 0 to {}:"
    "\nError: input must be an int between 0 and {}"

    pass  # this is a placeholder that you will replace with Python code


if __name__ == "__main__":
    main()

