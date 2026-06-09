import random
words = ["apple", "tiger", "house", "plant", "water"]
word = random.choice(words)
guessed_letters = []
wrong_guesses = 7
print("=== Welcome to Hangman Game ===")
while wrong_guesses > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct Guess!")
    else:
        wrong_guesses -= 1
        print("Wrong Guess!")
        print("Remaining chances:", wrong_guesses)
if wrong_guesses == 0:
    print("\n Game Over! The word was:", word)
    