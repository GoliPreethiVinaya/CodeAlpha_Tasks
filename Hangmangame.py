import random

words = ["apple", "banana", "orange", "grape", "mango"]
chosen_word = random.choice(words)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display.append("_")

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed '{guess}'.")

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("\n")
        print("EXCELLENT! \n")
        print("You guessed the word correctly. \n")

    if lives == 0:
        end_of_game = True
        print("GAME OVER!")
        print("The correct word was '{chosen_word}'.")


input("Press Enter to Exit....")
