#to remove the work form string
def remove_word(string, word):
    words = string.split()
    modified_words = [w for w in words if w.lower() != word.lower()]
    modified_string = ' '.join(modified_words)
    return modified_string

# Example usage
input_string = "Hello, world! Welcome to the world of programming."
word_to_remove = "world"

modified_string = remove_word(input_string, word_to_remove)
print("Modified string:", modified_string)
