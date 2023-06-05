import argparse
import hashlib
from prettytable import PrettyTable
import tkinter as tk
from tkinter import filedialog
import time

class PasswordHasher:
    def __init__(self):
        self.initialize = PrettyTable(["Input","Hash"])
        self.initialize.align = "c"
        self.table = []
        
    def open_file(self, input_file, output_file):
        try:
            with open(input_file, "r") as input_file, open(output_file, "w") as output_file:
                for line in input_file:
                    words = line.split()
                    for word in words:
                        hashed_word = hashlib.sha256(word.encode()).hexdigest()
                        self.table.append([word, hashed_word])
                        output_file.write(word + " " + hashed_word + "\n")

                for row in self.table:
                    self.initialize.add_row(row)
                    self.initialize.add_row(["", ""])
                print(self.initialize)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def hash_from_input(self, num_inputs):
        for i in range(num_inputs):
            try:
                user_input = input("Enter input {}: ".format(i+1))
                if user_input.lower() == 'exit':
                    break
                hashed_input = hashlib.sha256(user_input.encode()).hexdigest()
                self.table.append([user_input, hashed_input])
            except Exception as e:
                print(f"Error: {e}")

        for row in self.table:
            self.initialize.add_row(row)
            self.initialize.add_row(["", ""])
        print(self.initialize)

def print_ascii_art():
    ascii_art = ascii_art = r'''
 /$$   /$$            /$$$$$$  /$$       /$$ /$$          /$$ /$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$          
| $$  | $$           /$$__  $$| $$      | $$| $$         | $$| $$ /$$__  $$| $$____/  /$$__  $$| $$_____/          
| $$  | $$  /$$$$$$ | $$  \__/| $$$$$$$ | $$| $$ /$$$$$$ | $$| $$|__/  \ $$| $$      | $$  \__/| $$        /$$$$$$ 
| $$$$$$$$ |____  $$|  $$$$$$ | $$__  $$|__/|__/|____  $$|__/|__/  /$$$$$$/| $$$$$$$ | $$$$$$$ | $$$$$    /$$__  $$
| $$__  $$  /$$$$$$$ \____  $$| $$  \ $$         /$$$$$$$         /$$____/ |_____  $$| $$__  $$| $$__/   | $$  \__/
| $$  | $$ /$$__  $$ /$$  \ $$| $$  | $$        /$$__  $$        | $$       /$$  \ $$| $$  \ $$| $$      | $$      
| $$  | $$|  $$$$$$$|  $$$$$$/| $$  | $$       |  $$$$$$$        | $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$      
|__/  |__/ \_______/ \______/ |__/  |__/        \_______/        |________/ \______/  \______/ |________/|__/ 
'''
    print("\033[92m" + ascii_art + "\033[0m")
    print("by N1ght0Wl \n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hash passwords from a file or user input")
    parser.add_argument('-file', action='store_true', help='hash passwords from a file')
    parser.add_argument('-input', action='store_true', help='hash a specified number of user inputs')
    args = parser.parse_args()

    password_hasher = PasswordHasher()
    print_ascii_art()

    if args.file:
        root = tk.Tk()
        root.withdraw()
        input_file = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        output_file = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
        start_time = time.perf_counter()
        password_hasher.open_file(input_file, output_file)
        end_time = time.perf_counter()
        print(f"Execution time: {end_time - start_time:.3f} seconds")
    
    elif args.input:
        while True:
            try:
                num_inputs = input("Enter the number of inputs (use 'q' to quit): ")
                if num_inputs.lower() == 'q':
                    break
                num_inputs = int(num_inputs)
                start_time = time.perf_counter()
                password_hasher.hash_from_input(num_inputs)
                end_time = time.perf_counter()
                print(f"Execution time: {end_time - start_time:.3f} seconds")
            except ValueError as e:
                print(f"Error: {e}")
    else:
        print("Please provide either -file or -input argument.")

#BY N1ght0wl