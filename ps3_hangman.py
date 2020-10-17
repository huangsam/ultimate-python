# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):

    y=list(lettersGuessed)
    x=list(secretWord)
    return sorted(y) == sorted(x)
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...



def getGuessedWord(secretWord, lettersGuessed):
    for c in lettersGuessed and secretWord:
        
        if c in  lettersGuessed and secretWord :
        
            x =print(c, sep=' ', end='', flush=True)
        else:
            x =print(' _', sep=' ', end='', flush=True) #Printing FOR LOOP in One LIne!!!!!!!!!!
    return x



def getAvailableLetters(lettersGuessed):
    k ="abcdefghijklmnopqrstruvwxyz" 
    p=''.join(set(k).difference(lettersGuessed)) #minuses the no.s/alphabets from other
    w=sorted(p)       #even changes strings to lists
    print(''.join(w)) #joins the list into strings

    

    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    # FILL IN YOUR CODE HERE...i=
    print('these many letters : ', len(secretWord))
    
    lettersGuessed=str(input("guess the bloody alphabet"))
    
    while lettersGuessed!=secretWord:
    
    print(getAvailableLetters(lettersGuessed)) 
     
     lettersGuessed=str(input("guess the alphabet"))
       
         if userinput in secretWord:
         	 print(getGuessedWord(secretWord, lettersGuessed))
         	 print(getAvailableLetters(lettersGuessed))
         else :
         print(getAvailableLetters(lettersGuessed))	
          	

         




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
