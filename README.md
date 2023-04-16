# Password/String hasher by N1ght0wl

The Password Hasher is a Python script that allows you to hash passwords from a file or from user input using the SHA-256 hashing algorithm. It uses the `argparse ver == 1.4.0`, `hashlib ver == 0.0.1`, `prettytable ver == 2.2.0`, `tkinter ver == 8.6` `colorama ver == 0.4.4` and libraries.
This code was made with the `python version 3.8.0`, any other versions may cause errors.

## Functionality

The Password Hasher script provides two main functionalities:

1. Hashing passwords/strings from a file:
   - The `-file` command-line argument triggers this functionality.
   - It prompts the user to select an input file and an output file from windows explorer window.
   - It reads passwords/strings from the input file, hashes them using SHA-256, and writes the original passwords/strings along with their hashed values to the output file.
   - It displays the results in a formatted table using the `PrettyTable` library.
   - It measures the execution time and displays it at the end using the time library.

2. Hashing passwords/strings from user input:
   - The `-input` command-line argument triggers this functionality.
   - It prompts the user to enter the number of passwords they want to hash.
   - It reads the user inputs, hashes them using SHA-256, and displays the original passwords along with their hashed values in a formatted table using the `PrettyTable` library.
   - It measures the execution time and displays it at the end.

## Usage

To use the Password Hasher, follow these steps:

1. Install the required Python packages with `pip` and `requirements`:
   ```bash
   pip install -r requirements.txt
2. Choose the desired operation: "-input", "-file"
   ```bash
   python hasher.py -file
   or
   python hasher.py -input
3. The output should look something like this with the "-input" argument
   ```bash
    /$$   /$$            /$$$$$$  /$$       /$$ /$$          /$$ /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$
   | $$  | $$           /$$__  $$| $$      | $$| $$         | $$| $$ /$$__  $$| $$____/  /$$__  $$| $$_____/
   | $$  | $$  /$$$$$$ | $$  \__/| $$$$$$$ | $$| $$ /$$$$$$ | $$| $$|__/  \ $$| $$      | $$  \__/| $$        /$$$$$$ 
   | $$$$$$$$ |____  $$|  $$$$$$ | $$__  $$|__/|__/|____  $$|__/|__/  /$$$$$$/| $$$$$$$ | $$$$$$$ | $$$$$    /$$__  $$
   | $$__  $$  /$$$$$$$ \____  $$| $$  \ $$         /$$$$$$$         /$$____/ |_____  $$| $$__  $$| $$__/   | $$  \__/
   | $$  | $$ /$$__  $$ /$$  \ $$| $$  | $$        /$$__  $$        | $$       /$$  \ $$| $$  \ $$| $$      | $$      
   | $$  | $$|  $$$$$$$|  $$$$$$/| $$  | $$       |  $$$$$$$        | $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$      
   |__/  |__/ \_______/ \______/ |__/  |__/        \_______/        |________/ \______/  \______/ |________/|__/      

   Enter the number of inputs (or 'exit' to quit): 1
   Enter input 1: test
   +-------+------------------------------------------------------------------+
   | Input | Hash                                                             |
   +-------+------------------------------------------------------------------+
   | test  | 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08 |
   |       |                                                                  |
   +-------+------------------------------------------------------------------+
   Execution time: 1.513 seconds
   Enter the number of inputs (or 'exit' to quit): exit

4. Errors

   - Any error that may apper will be printed for user comprehension and correction
   - The user cannot use as input other than a .txt file for the "-file" option
   - Any number of hashes that is not a int, may cause errors

5. Questions that may come to mind
   - How can I use this program?
      - Ans: You can use this program to hash passwords and create rainbow tables
   - How many passwords can I hash with this program?
      - Ans: As many as you want, this program does not limit inputs, but your computer may have trouble to hash for example 1 milion strings
   - Is there any executable avaiable?
      - Ans: There is, I will enter a link to a cloud service that has all the executables for windows and linux
   - Does this program get detected by an antivirus?
      - Ans:
