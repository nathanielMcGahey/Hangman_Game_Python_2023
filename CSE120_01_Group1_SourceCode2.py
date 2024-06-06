import random
#This is the graphics function. This prints out the values of the letter guessed and what level of the hangman game the user is on
def updateGraphics(losses,letterList):
    #This is a list of all of the pictures of the hangman game
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
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
#This runs through the letter list and changes it from a list to a well looking graphic with missing letters represented by underscores and spaces between words represented too
    word = ""
    for x in range(len(letterList)):
        word = word + letterList[x] + " "
        
    print(HANGMANPICS[losses])
    print(word)
    
    #This tell the user how many losses they have left until they lose at the game
    print("You have", 6 - losses,"left until you lose")
    
    
    #This function allows the user to input a category and a difficulty which pulls a random word from the list
def randomWord():
    category = str(input("Which catagory would you like to play, animals, fruits, or colors? ")).lower()
    diff = int(input("Which difficutly would you like to play?: 0 - easy, 1 - medium, or 2 - hard: "))
    
    #Each of the different difficulties there are the 3 categorys and 5 words for each category
    if diff == 0: 
        words = {
        "animals": ["lion", "bear", "fish", "deer", "bird"],
        "fruits": ["apple", "banana", "orange", "grape", "kiwi"],
        "colors": ["red", "blue", "green", "yellow", "purple"]
        }
    elif diff == 1:
        words = {
        "animals": ["alligator", "racoon", "catfish", "whale", "peacock"],
        "fruits": ["fig", "blackberry", "watermelon", "coconut", "passionfruit"],
        "colors": ["aquamarine", "bubble gum", "charcoal", "crimson", "forest green"]
        }
    else:
        words = {
        "animals": ["chimpanzee", "black widow spider", "porcupine", "bearded dragon", "diplodocus"],
        "fruits": ["pomegranate", "plantain", "boysenberry", "african cherry orange", "papaya"],
        "colors": ["seafoam green", "candy apple red", "ocean boat blue", "outrageous orange", "pastel magenta"]
        }
    #This returns the random word from the catagory
    return random.choice(words[category])

 #This function asks for the input of the user for the letter they would like to guess
def askForLetter():
    return str(input("What letter would you like to guess: ")).lower()

#This function checks if the letter that the user guesses is right
def checkIfLetterIsRight(word,letter):
    isCorrect = False
    
    #This loops goes through all of the letters in the word to see if the letter inputed from the user matches what is actually in the word
    for l in word:
        if l == letter:
            print("You have gotten a letter right!")
            isCorrect = True
            break
    return isCorrect  

#This function updates the list that the updateGraphics uses for its function
def updateGraphicList(graphicList,letter,word):
    #This list goes through each of the letters of the word and will update the postion in the graphic list function with the letter instead of the underscore placeholder
    for l in range(len(word)):
            if word[l] == letter:
                graphicList[l] = word[l]

    return graphicList

#This function checks if the user wants to complete the word and will confirm or deny that the user has gotten the word correct
def checkIfWordIsComplete(word):
    #This checks if the user wants to guess the word
    check = int(input("Would you like to guess the word? 0 - no or 1 - yes: "))
    
    #This receves the input of the user they want to guess and will return if they got that right or wrong
    if check == 1:
        choiceWord = str(input("What word would you like to guess? ")).lower()
        if choiceWord == word:
            print("You have gotten the word correct! ")
            return True
        print("You have gotten the word incorrect. ")
    return False
        
#This function runs the whole game of hangman
def game(word):
    #These are the instant variables that are used by most functions
    graphicList = []
    losses = 0
    letterGuesses = []
    
    #This loop converts the word into underscores for graphic purposes while keeping the word variable intact to allow guessing of letters
    for x in word:
        if x == " ":
            graphicList.append(" ")
        else:
            graphicList.append("_")
    #This loops runs the game of hangman and will end when the user has won or lost
    while True:
        letter = askForLetter()
        
        #This will check if the letter that the user has guessed has already been guessed and will update the list if it is.
        check = False
        
        while True:
            for x in range(len(letterGuesses)):
                if letterGuesses[x] == letter:
                    check = True
                    break
            if check == True:
                print("You have already guessed this letter")
                letter = askForLetter()
            else:
                letterGuesses.append(letter)
                break
        #This will check if the user got the letter right, update the list of the graphic, and prints out the updated graphics
        if checkIfLetterIsRight(word, letter) == True:
            graphicList = updateGraphicList(graphicList,letter,word)
        else:
            losses = losses + 1
            print("You did not get a letter right." )
        updateGraphics(losses,graphicList)
        
        #This checks if the user has lose the game and tells the user the word 
        if losses == 6:
            print("You have lost. The word was", word)
            break
        
        #This will ask the user to complete the word if they wanted to and will end the program if they don't
        if checkIfWordIsComplete(word) == True:
            break
        
        
        
if __name__ == '__main__':
    #This runs the game with the ability to play again and end the game if the user wants to
    while True:
        
        #This creates the random word and uses the word to run the game
        word = randomWord()
        
        game(word)
        
        #The user selects if they would like to play the game again and will end the game if they do not
        cont = int(input("Would you like to play again? 0 - yes or 1 - no: "))
        
        if cont == 1:
            break
        
        
        
        
        
        
        