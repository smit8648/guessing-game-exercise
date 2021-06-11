import collections
import random


##created hangman visuals
def hangman_visual(tries_left):
    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
     |  |
     O  |
    /|  |
        |
        |
    =========''', '''
    +---+
     |  |
     O  |
    /|\ |
        |
        |
    =========''', '''
    +---+
     |  |
     O  |
    /|\ |
    /   |
        |
    =========''', '''
    +---+
     |  |
     O  |
    /|\ |
    / \ |
        |
    =========''']
    return(HANGMANPICS[tries_left])






##taking in an word and splitting it into a list of the letters
words_raw = open('words_alpha.txt')
words_list = words_raw.read().splitlines()


##function selects a random word using the random.choice operator and returns selected word
def getWord():
    word = random.choice(words_list)
    return(word)



# main function which takes in user input and compares it to random word
def playGame(word_guess):
    #variable instantiation 
    guess_loop = False
    guesscount = 7
    guesslist = []
    word_letters = []
    display_list = []
    win = False

    ## creates a string of _ elements the same length as random word
    for letter in word_guess:
        word_letters.append(letter.lower())
        display_list.append('_')
    ## checks the guesscount and win to ensure that the player has not exceeded their guesses or has won
    while guesscount > 0 and win == False:
        letter_guess = str(input("what is your guess: "))
        ##determines if the guess is the entire word or the letter
        if len(letter_guess) > 1:
            for letter in letter_guess:
                word_letters.append(letter.lower())

            ##if they correctly guess the word, this handles the win
            if collections.Counter(letter_guess) == collections.Counter(word_guess):
                        print("You win!")
                        win == True
                        return(1)
                        break
            
            ## handles if they guess the word guess and subtracts their guess count respectively
            else:
                print("guess again")
                guesscount -= 1
                
                
                if guesscount == 0:
                    print("you lose!")
        ## handles single letter input and compares the letter to the letters of the word_letters list using the indexes of the enumerate operator and a for loop
        elif len(letter_guess) == 1:   
            if letter_guess in guesslist:
                print("you already guessed that letter")

            ##checking to ensure that the input is actually a letter and not another character
            elif letter_guess.isalpha() == True:
                ##adds the input letter to the list of letters already guessed
                guesslist.append(letter_guess)

                ##enumerate indexes each letter within the word starting from zero. this is used to create a variable called indices, which is a list of the according indeces of the guessed letter
                if letter_guess in word_letters:
                    indices = [index for index, letters in enumerate(word_letters) if letter_guess == letters]
                    for index in indices:
                        display_list[index] = letter_guess
                    print(display_list)
                    ## this handles a comparison of the displayed _ list with guessed letters, and the original list of word letters (and handles wins)
                    if collections.Counter(display_list) == collections.Counter(word_letters):
                        print("You win!")
                        win == True
                        return(1)
                        break
                ## else case to catch if they incorrectly guessed, and if they lose
                else:
                    print("guess again")
                    guesscount -= 1
                    if guesscount == 0:
                        print("you lose!")
            ##catching if they entered a letter or not
            else:
                print("please enter a letter")
        #catches if they try to not input a value
        else:
            print("please enter a value")

        print(hangman_visual(-(guesscount)))






## function which can be called to run the hangman program by prompting user to play, and then generating a random word via getWord() and passing it to the playgame() function 
def hangman():
    wincount = 0
    losecount = 0
    result = 0
    usedwords = []

    while str(input("would you like to play? (y/n)")).lower() == "y":
        word = getWord()
        if word not in usedwords:
            usedwords.append(word)
            result = playGame(word)
            if result == 1:
                wincount += 1
            else:
                losecount += 1
            print(f"{wincount} wins.")
            print(f"{losecount} losses.")
    print("thanks for playing")

