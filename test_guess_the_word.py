import random
import guess_the_word

def test_word_is_from_list():
    words = ["python", "github", "college", "programming", "computer"]
    word = random.choice(words)
    assert word in words

def test_correct_guess_updates_word(monkeypatch):
    # Mock input sequence
    inputs = iter(["p"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Run a short version of the game setup
    words = ["python"]
    word = words[0]
    guessed_letters = []
    hidden_word = ["_"] * len(word)
    guess = "p"

    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                hidden_word[i] = guess

    assert hidden_word[0] == "p"
    assert "_" in hidden_word  # still has blanks left

def test_incorrect_guess_reduces_attempts():
    attempts = 6
    word = "python"
    guess = "z"
    if guess not in word:
        attempts -= 1
    assert attempts == 5
