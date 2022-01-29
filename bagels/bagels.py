import random 

NUM_DIGITS = 3 
MAX_GUESSES = 20

def  main():
  print( ''' Bagels, a deductive logic game. 
  
  I am Thinking of a {}- digit number with no repeated digits. 
  Try to guess what it is. Here are some clues: 
  When I say:    That means:
  Pico           One digit is correct but in the wrong position.
  Fermi          One digit is correct and in the right position.
  Bagels         No digit is correct.
  
  For example , if the secret number was 248 and your guess was 843, the 
  clues would be Fermi Pico. '''.format(NUM_DIGITS))
  
  while True: # main game loop
    secretNum = getSecretNumber()
    print('I have thought up a number.')
    print(' You have {} guesses to get it. ' .format( MAX_GUESSES))
    
    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
      guess = ' '
      # keep looping until they enter a valid guess:
      while len(guess) != NUM_DIGITS or not guess.isdecimal():
        print('Guess # {}: '.format(numGuesses))
        guess = input('> ')
     
      clues = getClues(guess,secretNum)
      print(clues)
      numGuesses+= 1
    
      if guess == secretNum:
        break # they're correct, so break out of this loop
      if numGuesses > MAX_GUESSES:
        print( 'You ran out of guesses! ')
        print(' The answer was {}.'.format(secretNum))
      
    #Ask the player if they want to play again
    
    print('Do you want to play again? (yes or no)' )
    if  not input('> ').lower().startwith('y')
      break
    
    
  print('Thanks for playing')
  

def getSecretNum():
  """ Returns a string made up of NUM_DIGITS unique random digits """
  number = list('0123456789') # create a list of digits 0-9
  random.shuffle(numbers) # shuffle them into random order 
  
  # get the first NUM_DIGITS digits in the list for the secret number:
  
  secretNum = ' '
  for i in range(NUM_DIGITS):
    secretNum+= str(numbers[i])
  return secretNum

def getClues ( guess, random):
  """ Returns a string with a pico, fermi, bagels clues for a guess and secret number pair"""
  if guess == secretNum:
    return 'You Got it!'
  
  clues = []
  
  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      clues.append('Fermi')
    elif guess[i] in secretNum:
      clues.append('Pico')
  if len(clues) == 0:
    return 'Bagels'
  else:
    clues.sort()
    return ' '.join(clues)
  
if _name_ =='_main_':
  main()
  
      
      
      
  
  
