import random

# Small cleanup and readability improvements

def guess_the_word():
    words = ["python", "github", "college", "programming", "computer"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Guess the Word.")
    print(f"The word has {len(word)} letters.")

    hidden_word = ["_"] * len(word)

    while attempts > 0 and "_" in hidden_word:
        print("\nWord:", " ".join(hidden_word))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter one letter at a time.")
            continue

        if guess in guessed_letters:
            print("You already tried that one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Nice, that one's in there.")
            for i, letter in enumerate(word):
                if letter == guess:
                    hidden_word[i] = guess
        else:
            print("Nope, not in the word.")
            attempts -= 1

    if "_" not in hidden_word:
        print(f"\nYou got it. The word was '{word}'.")
    else:
        print(f"\nYou're out of attempts. The word was '{word}'.")

if __name__ == "__main__":
    guess_the_word()
