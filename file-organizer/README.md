# file organizer 

a simple Python program that automatically organizes files in a folder into different categories based on their file extensions.

## features

* organizes images
* organizes documents
* organizes videos
* organizes music
* organizes archives
* organizes program files
* creates category folders automatically
* detects file extensions automatically
* moves files using Python's built-in libraries
* skips existing folders

## requirements

* Python 3.x
* no external libraries required

the project uses Python's built-in:

* `os`
* `shutil`

## how to run

1. clone or download this repository
2. open a terminal in the project folder
3. run:

```bash
python file_organizer.py
```

4. enter the path of the folder you want to organize

example:

```text
enter the folder path you want to organize: C:\Users\name\Downloads
```

the program will automatically create folders such as:

```text
Images/
Documents/
Videos/
Music/
Archives/
Programs/
Others/
```

and move the corresponding files into them.

## project structure

```text
file-organizer/
│
└── file_organizer.py
```

## concepts used

* variables
* dictionaries
* lists
* loops
* `if` statements
* functions
* string manipulation
* file paths
* file extensions
* `os.listdir()`
* `os.path`
* `os.makedirs()`
* `shutil.move()`
* exception handling

## screenshots
<img width="1365" height="419" alt="Screenshot 2026-09-03 163043" src="https://github.com/user-attachments/assets/688cb36e-a9e3-49ed-8af1-ace35da514a1" />
<img width="1363" height="346" alt="Screenshot 2026-09-03 163156" src="https://github.com/user-attachments/assets/2594ddca-131e-41d8-b9ea-c0e9f0afa4f5" />


## possible improvements

* add more file extensions
* allow custom categories
* add a graphical user interface
* detect duplicate files
* add an undo feature
* show a summary of how many files were moved
* allow users to choose which categories to organize
* organize files by date
* add a dry-run mode to preview changes before moving files

## note

this program actually moves files.

it is recommended to test it on a **dummy folder** first before using it on important files.

## license

this project is open-source and available for learning and personal use.
