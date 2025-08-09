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


# to initialize the class and use its methods
name = StringManipulator("Emam")

result = name.find_char('m')  
length = name.get_length()
uppercase = name.to_uppercase() 
print(f"Index of 'm': {result}")
print(f"Length of string: {length}")
print(f"Uppercase: {uppercase}")