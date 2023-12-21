###############################################################################
#   Computer Project #4
#
#   Algorithm
#     Start with main function for main program
#     fill out rest of 7 functions
#     Check for errors in inputs
#
#
###############################################################################
''' Insert heading comments here.'''
import math, string

# Define constants for punctuation and alphanumeric characters
#  string.punctuation is a string constant that contains all the punctuation characters on the keyboard.
#  except space is not included in this string
PUNCTUATION = string.punctuation

#  string.ascii_lowercase is a string constant that contains all the lowercase letters in the alphabet.
#  string.digits is a string constant that contains all the digits 0-9.
ALPHA_NUM = string.ascii_lowercase + string.digits


BANNER = ''' Welcome to the world of 'dumbcrypt,' where cryptography meets comedy! 
    We're combining Affine Cipher with Caesar Cipher to create a code 
    so 'dumb,' it's brilliant. 
    Remember, in 'dumbcrypt,' spaces are as rare as a unicorn wearing a top hat! 
    Let's dive into this cryptographic comedy adventure!             
    '''


def print_banner(message):
    '''Display the message as a banner.
    It formats the message inside a border of asterisks, creating the banner effect.'''
    border = '*' * 50
    print(border)
    print(f'* {message} *')
    print(border)
    print()

def multiplicative_inverse(A, M):
    '''Return the multiplicative inverse for A given M.
       Find it by trying possibilities until one is found.
        Args:
        A (int): The number for which the inverse is to be found.
        M (int): The modulo value.
        Returns:
            int: The multiplicative inverse of A modulo M.
    '''
    for x in range(M):
        if (A * x) % M == 1:
            return x


def check_co_prime(num, M):
    #finds GDC then checks if its equal to 1
    check = math.gcd(num,M)
    if check == 1:
        return True
    else:
        return False


def get_smallest_co_prime(M):
    #checks each number after one and up to M to check if its co prime
    for i in range(2,M):
        if check_co_prime(i,M) == True:
            return i


def caesar_cipher_encryption(ch, N, alphabet):
    #finds index of ch, encrypts, then finds the new character
    index = 0
    M = len(alphabet)
    for i,char in enumerate(alphabet):
        if char == ch:
            index = int(i)
            encryption = (index+N) % M
            for num, character in enumerate(alphabet):
                if num == encryption:
                    return character


def caesar_cipher_decryption(ch, N, alphabet):
    #finds index of ch, decrypts, then finds the new character
    index = 0
    M = len(alphabet)
    for i, char in enumerate(alphabet):
        if char == ch:
            index = int(i)
            encryption = (index - N) % M
            for num, character in enumerate(alphabet):
                if num == encryption:
                    return character


def affine_cipher_encryption(ch, N, alphabet):
    '''Insert a doc string here.'''
    M = len(alphabet)
    co_prime = get_smallest_co_prime(M)
    for i,char in enumerate(alphabet):
        if char == ch:
            index = int(i)
            encryption = (co_prime * index + N) % M
            for num, character in enumerate(alphabet):
                if num == encryption:
                    return character



def affine_cipher_decryption(ch, N, alphabet):
    '''Insert a doc string here.'''
    M = len(alphabet)
    co_prime = get_smallest_co_prime(M)
    inverse = multiplicative_inverse(co_prime,M)
    for i, char in enumerate(alphabet):
        if char == ch:
            index = int(i)
            encryption = inverse * (index - N) % M
            for num, character in enumerate(alphabet):
                if num == encryption:
                    return character


def main():
    print_banner(BANNER)
    # ask user to input roation
    z = 1
    while z > 0:
        rotation = input("Input a rotation (int): ")
        try:
            rotation = int(rotation)
            z = 0
        except ValueError:
            print("\nError; rotation must be an integer.")



       # check to see if rotation input is an integer if not print error
    y = 1
    while y > 0:
             #ask user to input command
        command = input("\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: ")
            #check to see if command input is e,d,or q if not
        #ask user to input a string
            #check to make sure there are no spaces
        if command == 'd':
            string = str(input("\nInput a string to decrypt: ")).lower()
            plain_text = ""
            space_count = 0
            for i in string:
                if i == " ":
                    space_count += 1
                    print("\nError with character:")
                    print("Cannot encrypt this string.")
                    break
                elif i.isalnum() == True:
                    decrypt_alph_num = str(affine_cipher_decryption(i,rotation,ALPHA_NUM))
                    plain_text += decrypt_alph_num

                else:
                    decrypt_pun = str(caesar_cipher_decryption(i,rotation,PUNCTUATION))
                    plain_text += decrypt_pun
            if space_count > 0:
                space_count = 0
            else:
                print("\nCipher text:", string)
                print("\nPlain text:", plain_text)

        elif command == 'e':
            string = str(input("\nInput a string to encrypt: ")).lower()
            cipher_text = ""
            space_count = 0
            for i in string:
                if i == " ":
                    space_count += 1
                    print("\nError with character:")
                    print("Cannot encrypt this string.")
                    break
                elif i.isalnum() == True:
                    encrypt_alph_num = str(affine_cipher_encryption(i, rotation, ALPHA_NUM))
                    cipher_text += encrypt_alph_num

                else:
                    encrypt_pun = str(caesar_cipher_encryption(i, rotation, PUNCTUATION))
                    cipher_text += encrypt_pun
            if space_count > 0:
                space_count = 0
            else:
                print("\nPlain text:", string)
                print("\nCipher text:", cipher_text)

        elif command == "q":
            y = 0

        else:
            print("\nCommand not recognized.")





    "Input a rotation (int): "
    "\nError; rotation must be an integer."
    "\n\nInput a command (e)ncrypt, (d)ecrypt, (q)uit: "
    "\nInput a string to encrypt: "
    "\nError with character:"
    "Cannot encrypt this string."
    "\nPlain text:"
    "\nCipher text:"
    "\nCommand not recognized."
# These two lines allow this program to be imported into other codes
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
# DO NOT CHANGE THESE 2 lines or Do NOT add code to them. Everything
# you add should be in the 'main' function above.
if __name__ == '__main__':
    main()



