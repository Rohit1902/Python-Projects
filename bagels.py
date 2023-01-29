# Python program to pla the game 'BAGELS'
import random
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f'''Bagels, a deductive logic game.
    I am thinking of a {NUM_DIGITS}-digits number with no repeated digits.
    Try to guess what it is. Here are some clues : 
    When I say :        That means :
        Pico                One digit is correct but in wrong position
        Fermi               One digit is correct in correct position
        Bagels              No digit is correct
        
    e.g.  if the number was 24 and your guess was 84 , clues would be Fermi ''')

    while True:     #main game loop
        #This stores the secret number the player needs to guess
        secretNum = getSecretNum()
        print("I have thought of a number.")
        print(f"You have {MAX_GUESSES} guesses to get it")

        numGuess = 1
        while numGuess<=MAX_GUESSES:
            guess = ''
            # Keep looping until a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
            # no of digits not equal or guess is not a decimal number(digits in 0-9)
                print(f'Guess #{numGuess} : ')
                guess = input('> ')

            clues = getClues(guess,secretNum)
            print(clues)
            numGuess+=1

            if guess==secretNum:
                break #They are correct , so break out of loop 
            if numGuess > MAX_GUESSES:
                print("You ran out of guesses.")
                print(f"The answer was {secretNum}")

        # Ask player if they want to play again
        print('Do you want to play again ? (yes/no)')
        if not input('> ').lower().startswith('y'):
            break   #i.e if input is not yes
        print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits"""   
    numbers = list('0123456789')  #Creating list of digits from 0-9
    random.shuffle(numbers)   #Shuffle into random order
    # Get the first NUM_DIGITS digits in the list for the secret number:    
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum+=str(numbers[i])
    return secretNum


def getClues(guess,secretNum):
    """Returns a string with pico,fermi , bagels clues for a guess
    and a secret number pair."""
    if guess==secretNum:
        return 'You got it!'

    clues = []
    
    for i in range(len(guess)):
        if guess[i]==secretNum[i]:
        # correct digit in correct postion
            clues.append('Fermi')
        elif guess[i] in secretNum:
        # correct digit in wrong position
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagels' # No correct digits at all
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away
        clues.sort()
        #Make a single string from list of string clues
        return ' '.join(clues)

# If program is run (instead of imported), run the game:
# if __name__=='__main()__':
main()






