import random

def get_random_word():
    # You can expand this list or load from a file
    words = ['python', 'hangman', 'challenge', 'programming', 'algorithm', 'computer']
    return random.choice(words).lower()

def display_word(word, guessed_letters):
    # This function displays the word with guessed letters revealed and underscores for unguessed letters
    displayed = ''.join(letter if letter in guessed_letters else '_' for letter in word)
    return displayed

def play_game():
    word = get_random_word()
    guessed_letters = set()
    # Initialize lives specially for the game lives
    lives = 6

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {len(word)} letters.")
    print(display_word(word, guessed_letters))

    while lives > 0:
        guess = input("Guess a letter: ").lower()

        # Input validation - ensure single letter and alphabetic
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            lives -= 1
            print(f"Wrong guess! You lost a life. Lives remaining: {lives}")
        
        # Display the current state of the word to call the display_word function
        current_display = display_word(word, guessed_letters)
        print(current_display)

        if '_' not in current_display:
            print("Congratulations! You guessed the word correctly!")
            break
    else:
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    play_game()