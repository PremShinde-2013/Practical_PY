#to read the file and to cpaitalize the first letter in the file
def capitalize_first_letter(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        capitalized_content = content.title()

        with open(output_file, 'w') as file:
            file.write(capitalized_content)

        print("File '{}' capitalized successfully and saved as '{}'.".format(input_file, output_file))
    except IOError:
        print("An error occurred while processing the file.")

# Example usage
input_file = "input.txt"
output_file = "output.txt"

capitalize_first_letter(input_file, output_file)
