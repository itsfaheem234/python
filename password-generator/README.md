# password generator 

a simple command-line password generator built with Python. it creates random passwords using letters, with optional numbers and symbols.

## features

* choose the password length
* include uppercase and lowercase letters
* optionally include numbers
* optionally include symbols
* generates a new random password each time
* handles invalid length input
* simple command-line interface

## requirements

* Python 3.x

no external libraries are required.

## how to run

1. clone or download the repository.
2. open a terminal in the project folder.
3. run:

```bash
python password_generator.py
```

4. enter the desired password length.
5. choose whether to include numbers and symbols.
6. copy the generated password.

## example

```text
===== PASSWORD GENERATOR =====

enter password length: 16
include numbers? (y/n): y
include symbols? (y/n): y

generated password:
G7@kP2!xQ9#mL4$z
```

the generated password will be different each time.

## concepts used

* functions
* strings
* loops
* conditional statements
* `random`
* `string`
* `random.choice()`
* user input
* `try/except`

## screenshot
<img width="1365" height="719" alt="image" src="https://github.com/user-attachments/assets/54a4d1de-95a7-4f4c-8a5c-1b8823ec58f5" />


## possible improvements

* guarantee at least one number when numbers are enabled
* guarantee at least one symbol when symbols are enabled
* add a password strength checker
* use Python's `secrets` module for security-focused generation
* add an option to generate multiple passwords
* add a graphical user interface

## license

this project is open source and available for personal and educational use.
