#program to check whether given sub string is present in given string
def check_substring(string, substring):
    if substring in string:
        return True
    else:
        return False

# Example usage
input_string = "This is a sample string."
search_substring = "sample"
is_present = check_substring(input_string, search_substring)
if is_present:
    print("The substring '{}' is present in the string.".format(search_substring))
else:
    print("The substring '{}' is not present in the string.".format(search_substring))

