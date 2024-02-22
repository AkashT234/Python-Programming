class StringReverser:
    def reverse_words(self, input_string):
        words = input_string.split()
        reversed_string = ' '.join(reversed(words))
        return reversed_string

# Example usage:
if _name_ == "_main_":
    reverser = StringReverser()
    input_string = input("Enter a string: ")

    reversed_result = reverser.reverse_words(input_string)
    print(f"Reversed string (word by word): {reversed_result}")
