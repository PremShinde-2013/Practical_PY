#length of string using recursion
def calculate_length(string):
    if string == '':
        return 0
    else:
        return 1 + calculate_length(string[1:])

# Example usage
input_string = "Hello, World!"

length = calculate_length(input_string)
print("Length of the string:", length)
