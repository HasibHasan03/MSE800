class StringManipulator:
    # def __init__(self, text):
    #     self.text = text
    ## 
    # if I don't initialize text, it will raise an error when calling methods that use it. 
    # Error look like: TypeError: StringManipulator() takes no arguments 
    # ##
    
    def find_char(self, char):
        return self.text.find(char)

    def get_length(self):
        return len(self.text)
    
    def to_uppercase(self):
        return self.text.upper()

    def to_lowercase(self):
        return self.text.lower()

def main():
    # Emam usage of the StringManipulator class and its methods
    manipulator = StringManipulator("Emam")
    print(f"Index of 'm' {manipulator.find_char('a')}")  
    print(f"Length of string: {manipulator.get_length()}")     
    print(f"Uppercase: {manipulator.to_uppercase()}")   
    print(f"Lowercase: {manipulator.to_lowercase()}")   

if __name__ == "__main__":
    main()