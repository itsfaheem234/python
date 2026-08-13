# hangman
a simple command-line hangman game built in *Python*, where the player tries to guess a randomly selected word one letter at a time

## about the game
the game randomly selects a word from a predefined word bank. the player guesses letters individually and has a limited number of incorrect guesses before the game ends.

instead of traditional hangman **ASCII** art, this version uses tally marks (|) to represent incorrect guesses.

## how to play
1. run the Python program
2. a random word will be selected
3. guess one letter at a time
4. correct guesses reveal the letter's position in the word
5. incorrect guesses add a tally mark (|)
6. guess the entire word before reaching the maximum number of incorrect guesses
7. choose whether to play again after each game

## example
Word: ```_ _ t _ _ n```

Guessed letters: a e t 

Incorrect guesses: ||| 

Enter a letter: 

## features
1) random word selection
2) letter-by-letter guessing
3) limited incorrect guesses
4) tally-mark system for incorrect guesses
5) input validation
6) replay functionality
7) tracks guessed letters during each game

## concepts used
1) variables
2) lists
3) sets
4) strings
5) ```if/elif/else``` statements
6) ```for``` and ```while``` loops
7) functions
8) random number generation
9) user input
10) input validation
11) ```all()``` function
12) basic program structure using ```if __name__ == "__main__"```

## gameplay
<img width="1363" height="720" alt="Screenshot 2026-08-13 100744" src="https://github.com/user-attachments/assets/d15eedc6-21b0-4142-922d-557949b4c96b" />


## built with
python 3

## future improvements
1) larger word bank
2) word categories such as animals, technology, countries, etc
3) difficulty levels
4) hint system
5) score and high-score tracking
6) win/loss statistics
7) win streak tracking
8) store the word bank in a separate ```.txt``` or ```.json``` file

## what i learned
this project helped me practice organizing a *Python* program using functions, loops, collections, conditionals, randomness, and input validation

it also introduced the idea of separating different parts of a program into functions, making the code easier to understand and modify

## author
faheem
