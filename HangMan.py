#A hangman game where the user must guess the computer's word before being hanged
#inspired by "selftaught.blog" tutorial for hangman

import random


wordCollection = ["person","linen","boundary","hill","substance","interest","wish","ducks"]
randomWord = wordCollection[random.randrange(0,len(wordCollection))]


def main():
    hangMan(randomWord)

#code to return a letter guessed by the user
def userGuessLetter():
    while True:
        userInput = str(input("Guess a letter: "))
        if len(userInput) != 1:
            print("Must be a letter only")
        else:
            return userInput

#function if the game is won
def gameWon(word):
    print("Congratulations! You guessed right!")
    print("The word to guess was: ", word)
    exit()

#function if the game is lost
def gameOver():
    print("Game Over!")
    print("You ran out of guesses :(")
    print("May you swing in peace!")

#main game
def hangMan(word :str):
    wrongGuesses = 0
    rightGuesses = 0
    lettersUsed = []
    stages = ["_______ ", "|  | ", "|  0 ", "|  /|\ ", "|  / \ ", "| ", "|[^^^^^^^]"]
    board = ["_"] * len(word)
    wordList = list(word)
    print("Let's play Hangman!")
    print("\n")

    #loop of the game
    while wrongGuesses < len(stages):
        print("\n")
        #print the board (hidden word to guess)
        print("The word to guess is: ")
        for boardSpace in board:
            print(boardSpace, end="")
        print("\n")
        userLetter = userGuessLetter()
        #check if letter is already guessed
        if userLetter not in lettersUsed:
            lettersUsed.append(userLetter)

            #if player guessed a letter correctly
            if (userLetter in wordList):
                rightGuesses += 1
                print("You guessed right!")
                occurances = [index for index, element in enumerate(word) if element == userLetter]
                for index in occurances:
                    board[index] = userLetter
            
                #if all the letters were guessed, win logic
                if rightGuesses == len(word) - 1:
                    gameWon(word)

            else:
                for stage in stages[0:wrongGuesses + 1]:
                    print(stage)
                wrongGuesses += 1
        
        #if user already guessed the same letter
        else:
            print("You already used that letter")
            print("Letters already guessed: ", lettersUsed)
        
    
    #logic if game lost
    gameOver()

    

if __name__ == "__main__":
    main()
