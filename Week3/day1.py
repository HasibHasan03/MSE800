import os


class FileReader:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def read_file(self):
        """Read the file and store lines in self.data"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:  # specify UTF-8
                self.data = [line.strip() for line in file]  # remove newline characters
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
        except UnicodeDecodeError:
            print(f"Error: Cannot decode file '{self.filename}'. Check encoding.")
    # thsis method reads the file and stores each line in self.data at the last index
    def append_to_file(self, text):
        """Append a new line to the file"""
        try:
            with open(self.filename, 'a', encoding='utf-8') as file:  # 'a' mode = append
                file.write(text + '\n')
            print(f"Successfully appended: {text}")
        except Exception as e:
            print(f"Error writing to file: {e}")

    # task 2: to count the total words in the file
    def count_words(self):
        """Count total words in the file"""
        total_words = sum(len(line.split()) for line in self.data)
        print(f"Total words in the file: {total_words}")
        return total_words
    
    def display_data(self):
        """Print the data"""
        for line in self.data:
            print(line)  

# --- Using the class ---
os.chdir("E:/Applications/Python/MSE800/Week3")

reader = FileReader("demo.txt")
# reader = FileReader("E:/Applications/Python/MSE800/Week3/demo.txt")  # create object

# Append new lines
reader.append_to_file("This new line: Emam Hasan")

reader.read_file()               # read the file
reader.display_data()            # show the content
reader.count_words()             # count words in the file