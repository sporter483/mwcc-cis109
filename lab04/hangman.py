import random

wordlist = [
    "Kelce",
    "Swiftie",
    "Taylor"
]
word_index = random.randint(0, len(wordlist) -1)
word = wordlist[word_index].lower()

bad_guesses = []

board = []
for letter in word:
     board.append("_")

while True:
    print("Welcome to Hangman!")

    print(board)
    print(bad_guesses)

    guess = input("Enter your guess:")

    if len(guess) != 1:
        print("Invalid input. Please enter one letter.")
        continue

    if guess in bad_guesses:  
        print("You already guessed that letter!")
        input("Press [enter] to continue.")
        continue

    if guess not in word:
        bad_guesses.append(guess)

        if len(bad_guesses) == 1:
            print("+---+)")
            print("|")
            print("|")
            print("|")
            print("|")
            print("======")
        if len(bad_guesses) == 2:
          print("+---+)")
          print("|   |")
          print("|")
          print("|")
          print("======")
        if len(bad_guesses) == 3:
            print("+---+)")
            print("|   |")
            print("|   O")
            print("|")
            print("|")
            print("======")
        if len(bad_guesses) == 4:
            print("+---+)")
            print("|   |")
            print("|   O")
            print("|   |")
            print("|")
            print("======")
        if len(bad_guesses) == 5:
            print("+---+)")
            print("|   |")
            print("|   O")
            print("|  /|\\")
            print("|")
            print("======")
        if len(bad_guesses) == 6:
            print("+---+)")
            print("|   |")
            print("|   O")
            print("|  /|\\")
            print("|  / \\")
            print("======")
            print("YOU LOST! The word was",word)
            break

        print(guess, "is not in the word!")
        input("Press [enter] to continue.")
        continue
    for i in range(len(word)):
        if word[i] == guess:
            board[i] = guess
    print(guess, "is in the word!")
    input("Press [enter] to continue.")

    if "_" not in board:
        print("You WON! The word was", word)
        break
print("Thank you for playing!")