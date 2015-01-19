__author__ = 'victoriabetts'
import random

maxWords = 125
i = 0
wordList = []
guesses = set([])
filename = 'wordlist.txt'
file = open(filename)

gallows = [
    [' ', ' ', ' ', ' ', '_', '_', '_', '_','_', '_', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' '],
    [' ', ' ', ' ', '{', ' ', '}', ' ', ' ', ' ', '|',' ', ' ', ' '],
    [' ', ' ', '/', ' ', '|', ' ', '\\', ' ', ' ', '|',' ', ' ', ' '],
    [' ', '/', ' ', ' ', '|', ' ', ' ', '\\', ' ', '|',' ', ' ', ' '],
    [' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', ' ', '|',' ', ' ', ' '],
    [' ', ' ', '/', '_', '_', '_', '\\', ' ', ' ', '|',' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', '_', '_', '_', '|','_', '_', '_']
]

hangman = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 2, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 6, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 5, 5, 5, 6, 6, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

while (i <= maxWords):
    word = file.readline()
    wordFix = word.replace('\n', '')
    wordList.append(wordFix)
    i+=1
    
def GetWord():
    wordNum = random.randint(0, maxWords)
    global word
    word = wordList[wordNum]
    return word
    
def PrintScreen(word, letters):
    wordLength = len(word)
    i = 0
    lineList = []
    str = " "
    drawing = []

    while (i <= wordLength-1):
        lineList.append('__')
        i+=1
    
    for (i, letter) in enumerate(word):
        if letter in guesses:
            lineList[i] = letter
    print ("")
    print ("Letters you have guessed: ")
    
    printGuess = []
    for guess in guesses:
        printGuess.append(guess)
        
    print(' '.join(printGuess))

                
    DrawHangman(letters)
    print(''.join(drawing))
    print ('')
    print (str.join(lineList))
    
    
    
def DrawHangman(letters):
    lines = []
    
    for row in range(len(hangman)):
        line = []
        for column in range(len(hangman[row])):
            if hangman[row][column] <= len(guesses - letters):
                line.append(gallows[row][column])
            else:
                line.append(" ")
        lines.append("".join(line))
    print ("")
    print ('\n'.join(lines))

MAX_TRIES = 6
        
def GetGuess():
    guess = input('Guess a letter: ')
    if guess in guesses:
        print("You've already guessed that letter. Try again.")
        return guess
    else:
        return guess

def main():
    word = GetWord().lower()
    correctLetters = set(word)
    PrintScreen(word, correctLetters)
    while len(guesses-correctLetters) < MAX_TRIES and len(correctLetters - guesses) > 0:
        attempt = GetGuess()
        guesses.add(attempt)
        PrintScreen(word, correctLetters)
    
    if len(correctLetters - guesses) == 0:
        print ("Yay! You win!")
    else:
        print ("You lose! Booo")
        print ("Your word was " + word)
    
    

main()
    
