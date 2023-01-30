"""
File: word_guess.py
-------------------
A simple hangman word guessing game.
"""

import random
import tkinter

CANVAS_WIDTH = 600  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600  # Height of drawing canvas in pixels

LEXICON_FILE = "Lexicon.txt"  # File to read word list from
INITIAL_GUESSES = 8  # Initial number of guesses player starts with

def main():
    """
    To play the game, we first draw the canvas, then select the secret word for
    the player to guess and then play the game using that secret word.
    """

    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Hangman')
    make_gallows(canvas)

    secret_word = get_word()
    play_game(canvas, secret_word)

def get_word():
    """
    This function returns a secret word that the player is trying to guess in
    the game.  This function initially has a very small list of words that it
    can select from to make it easier for you to write and debug the main game
    playing program.  In Part II of writing this program, you will re-implement
    this function to select a word from a much larger list by reading a list of
    words from the file specified by the constant LEXICON_FILE.
    """

    word_list = []
    for line in open(LEXICON_FILE):
        line = line.strip()
        word_list.append(line)

    random_word = random.choice(word_list)
    return random_word


def play_game(canvas, secret_word):
    """
    Add your code (remember to delete the "pass" below)
    """

    current_guesses = INITIAL_GUESSES
    num_misses = 0
    game = True

    unknown_word = hide_characters(secret_word)
    display_word = ''.join(unknown_word)

    print("")
    while game:
        print("The word now looks like this: " + str(display_word))

        print("You have " + str(current_guesses) + " guesses left.", "\n")

        letter_guess = input("Type a single letter here, then press enter: ")
        letter_guess = letter_guess.upper()

        if letter_guess == '':
            print("Please guess a letter.")
        elif len(letter_guess) > 1:
            print("Guess should only be a single character.")
        elif (letter_guess in secret_word) and (letter_guess not in display_word):
            print("That guess is correct.")
            display_word = add_letters(secret_word, display_word, letter_guess)
            display_word = ''.join(display_word)
        elif (letter_guess in secret_word) and (letter_guess in display_word):
            print("You have already guessed: " + str(letter_guess) + ", please guess a new letter.")
        else:
            current_guesses -= 1
            num_misses += 1
            draw_body(canvas, num_misses)
            print("There are no " + str(letter_guess) + "'s in the word.", "\n")

        if current_guesses == 0:
            print("Sorry, you lost. The secret word was: " + str(secret_word), "\n")
            game = False
            play_again = input("Press 'y' to play again, 'n' to quit.")
            if play_again == "y":
                canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Hangman')
                make_gallows(canvas)
                current_guesses = INITIAL_GUESSES
                num_misses = 0
                game = True
                secret_word = get_word()
                unknown_word = hide_characters(secret_word)
                display_word = ''.join(unknown_word)
                print("")
            else:
                break

        if display_word == secret_word:
            print("")
            print("Congratulations, the word is: " + str(secret_word), "\n")
            game = False
            play_again = input("Press 'y' to play again, 'n' to quit.")
            if play_again == "y":
                canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Hangman')
                make_gallows(canvas)
                current_guesses = INITIAL_GUESSES
                num_misses = 0
                game = True
                secret_word = get_word()
                unknown_word = hide_characters(secret_word)
                display_word = ''.join(unknown_word)
                print("")
            else:
                break

def draw_body(canvas, num_misses):
    match num_misses:
        case 1:
            # draw head
            canvas.create_oval(225, 150, 275, 200, outline="blue")
        case 2:
            # draw neck
            canvas.create_line(250, 200, 250, 215, fill="blue")
        case 3:
            # draw body
            canvas.create_rectangle(225, 215, 275, 350, outline="blue")
        case 4:
            # draw left arm
            canvas.create_line(225, 225, 200, 210, fill="blue")
        case 5:
            # draw right arm
            canvas.create_line(275, 225, 300, 210, fill="blue")
        case 6:
            # draw left leg
            canvas.create_line(240, 350, 215, 375, fill="blue")
        case 7:
            # draw right leg
            canvas.create_line(260, 350, 285, 375, fill="blue")
        case 8:
            # draw sad face
            canvas.create_line(233, 165, 237, 165, fill="blue")
            canvas.create_line(263, 165, 267, 165, fill="blue")
            canvas.create_oval(245, 175, 255, 185, fill="blue")

def make_gallows(canvas):
    # gallows posts (right and bottom)
    canvas.create_line(500, 100, 500, 500, fill="red")
    canvas.create_line(100, 500, 500, 500, fill="red")
    # gallows top post
    canvas.create_line(250, 100, 500, 100, fill="red")
    # gallows hanging post
    canvas.create_line(250, 100, 250, 150, fill="red")

    canvas.create_text(25, 560, anchor='w', font='Courier 52', text='H A N G M A N', fill="red")


def add_letters(secret_word, display_word, letter_guess):
    new_string = []
    for letter in secret_word:
        if letter_guess == letter:
            new_string.append(letter)
        elif letter in display_word:
            new_string.append(letter)
        else:
            new_string.append("-")
    return new_string


def hide_characters(secret_word):
    hidden_word = []
    for letter in secret_word:
        if letter != "-":
            hidden_word.append('-')
        else:
            hidden_word.append(letter)
    return hidden_word


def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas of the given int size with a blue
    border, ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == "__main__":
    main()
