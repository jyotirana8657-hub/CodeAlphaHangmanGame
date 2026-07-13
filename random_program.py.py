import random

word_list = ["python", "hangman", "laptop", "guitar", "pencil"]

secret_word = random.choice(word_list)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("Try to guess the word one letter at a time.")
print("You have", max_incorrect, "incorrect guesses allowed.\n")

while incorrect_guesses < max_incorrect:

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter + " "
        else:
            display_word = display_word + "_ "

    print("Word: " + display_word)
    print("Incorrect guesses remaining:", max_incorrect - incorrect_guesses)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word: " + secret_word)
        break

    guess = input("Guess a letter: ").lower().strip()


    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try a different one.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
    else:
        incorrect_guesses = incorrect_guesses + 1
        print("Wrong guess!\n")

if incorrect_guesses == max_incorrect:
    print("You have run out of guesses!")
    print("The word was: " + secret_word)

print("\nThanks for playing Hangman!")
