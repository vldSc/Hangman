import random
from replit import clear
from art import stages, logo, word_list, alpha


def continue_game():
    while True:
        answer = input("Do you want to play again? 'Y' for yes, 'N' for no: ").lower()
        if answer in ["y","n"]:
            break
        else:
            print("Answer is not valid!")
    return answer

yn = True

while yn:

    clear()

    lives = 6
    letters = []

    word = random.choice(word_list)
    print(f"Word is {word}")

    n = len(word)

    word_guess = []

    for _ in word:
        word_guess += '_'

    print(logo)
    print(' '.join(word_guess))
    end_game = False

    while not end_game:
        print(f"\nRemaining lives:{lives}\n{stages[lives]}")
        guess = input ("Guess a letter: ").lower()

        clear()
        

        if guess in letters:
            print(f"You already choose this letter! Try again! The letters you chose: {', '.join(letters)} ")
            print(' '.join(word_guess))
            continue

        if guess not in alpha:
            print("Please, chose a LETTER!")
            print(' '.join(word_guess))
            continue

        for i in range(n):
            if guess == word[i]:
                word_guess[i] = guess
                letters += guess
        print(' '.join(word_guess))
        
        if guess not in word:
            lives -=1
            print(f"Ups, you chose letter {guess}, that's not in the word! You lose a live!")
            letters += guess
            if lives == 0:
                end_game = True
                print(' '.join(word_guess))
                print(f"\nGame over! The word is {word}\n{stages[lives]}")

                choices = continue_game()

                if choices == 'n':
                    print("See you next time!")
                    yn = False
                    
        if "_" not in word_guess:
            end_game = True
            print(f"You win!\nThe word is {word}.")

            choices = continue_game()

            if choices == 'n':
                print("See you next time!")
                yn = False
        


