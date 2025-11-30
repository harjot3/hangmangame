# in this code im going to be trying to make the hangman game
# what i'll need to do:
# fetch a random word,
# if the user gets a letter right, then I fill that letter in, 
# else, they lose on of their 6 guesses
import random
playGame = True
INCORRECT_WORDS = ['!@#$%^&*(){\}"`~;:.,/\+=-0_?><']

def my_function():
    answer = 3
    while (answer != 1 and answer != 2):
        print("Would you like to play again?\n1. Yes\n2. No")
        try:
            answer = int(input("Enter here: "))
        except ValueError:
            pass
    return answer == 1

while playGame:
    # later this will fetch large database of words
    words = ["apples", "bananas", "carrots"]
    word = random.choice(words)
    wordList = list(word)
    # print(wordList)
    counter = 6

    print("The length of your word is", len(wordList))
    while counter > 0 and len(wordList) > 0:
        guess = input("Guess a letter: ")
        print("-"*75)
        try:
            # test if the input is a number
            test = float(guess)
            if (guess in list(INCORRECT_WORDS)):
                raise Exception(guess,"is not a letter.")

        except ValueError: # if there is error -> meaning the input is not number
            # print("your input wasn't a number, great!")
            if (len(guess) > 1): 
                print("but you need to guess a single letter\n")
            else:
                # print("and your answer was a single letter!")
                if (guess in word):
                    # print("on top of that your guess was in the word!")
                    tempCounter = 0
                    while (guess in wordList):
                        wordList.remove(guess)
                        tempCounter +=1
                    print("there are",tempCounter,"instance(s) of",guess,"in the word, the length of the word is now", len(wordList))
                    if (len(wordList) == 0):
                        print("Congrajulations! You've beaten the Hangman game")
                        playGame = my_function()
                else:
                    counter -= 1
                    print("there are 0 instance(s) of",guess,"in the word, you now have", counter, "guesses left.")
                    if (counter == 0):
                        playGame = my_function()

        else: # if there is no error, meaning input is a number
            print("your input was not a letter, try again:")
