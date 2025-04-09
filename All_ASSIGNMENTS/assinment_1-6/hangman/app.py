import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 7

    #getting user input
    while len(word_letters) > 0 and lives > 0:
      print('You have used these letter: ', ' '.join(used_letters))

      word_list = [letter if letter in used_letters else '-' for letter in word]
      print('Current words: ', ' '.join(word_list))
      
      user_letter = input('Guess a letter: ').upper()
      if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        
        else:
           lives = lives - 1
           print(f'Letter is not in word. You have {lives} lives left')
    
      elif user_letter in used_letters:
        print("You have already used that letter character. Please try again.")

      else:
        print('Invalid character. Please try again.')

    if lives == 0:
       print('You died, Sorry. The word was ', word)
    else:
       print('Yas! You guessed the word', word, '!!')


hangman()
       