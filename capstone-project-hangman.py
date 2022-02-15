
import random
# more word list importing: this is just imaginary
# form hangman_words import word_list
word_list = ["advark", "baboon", "camel", "children", "computer", "science", "people", "encyclopaedia", "examiner", "internet", "programming", "intelligence", "people", "abruptly", "absurd", "modules", "kindergarten", "personnae"]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word = random.choice(word_list) 

display = []
# generating dashes as many as the number of letters in the chosen word
for _ in chosen_word:
    display.append("_")

# maximum of six lives
lives = 6

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # checking if the guessed word is in the chosen word
    if guess in display:
        print(f"{guess} hass already been guessed.")
    
    # replacing the corresponding dash with the correctly guessed letter
    for letter_pos in range(len(chosen_word)):
        if guess == chosen_word[letter_pos]:
            display[letter_pos] = guess

    # punishing the player if the input the wrong word
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"{guess} is not in the secret word.")
        if lives == 0:
            print(f"GAME OVER. YOU LOST. THE WORD WAS {chosen_word}")
            end_of_game = True

    print(''.join(display))
    if "_" not in display:
        end_of_game = True
        print("You win")