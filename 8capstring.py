#to read the file and to capitalize the string
def capitalize_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        capitalized_content = content.upper()

        with open(output_file, 'w') as file:
            file.write(capitalized_content)

        print("File '{}' capitalized successfully and saved as '{}'.".format(input_file, output_file))
    except IOError:
        print("An error occurred while processing the file.")

# Example usage
input_file = "input.txt"
output_file = "output.txt"

capitalize_file(input_file, output_file)
