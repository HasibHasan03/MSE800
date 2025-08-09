class StringManipulator:
    def __init__(self, text):
        self.text = text
    
    def find_char(self, char):
        return self.text.find(char)

    def get_length(self):
        return len(self.text)
    
    def to_uppercase(self):
        return self.text.upper()

    def to_lowercase(self):
        return self.text.lower()
    
    def word_count(self):
        return len(self.text.split())

def main():
    # Emam usage of the StringManipulator class and its methods
    manipulator = StringManipulator("Emam is learning Python")
    print(f"Index of 'm' {manipulator.find_char('a')}")  
    print(f"Length of string: {manipulator.get_length()}")     
    print(f"Uppercase: {manipulator.to_uppercase()}")   
    print(f"Lowercase: {manipulator.to_lowercase()}")  
    print(f"Word count: {manipulator.word_count()}") 

if __name__ == "__main__":
    main()