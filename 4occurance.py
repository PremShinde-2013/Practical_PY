#program to find out occurrence of the word in given string
def count_occurrences(string, word):
    words = string.lower().split()
    count = 0
    for w in words:
        if w == word.lower():
            count += 1
    return count

# Example usage
input_string = "This is a sample string. String is repeated multiple times in this string."
search_word = "string"

occurrence_count = count_occurrences(input_string, search_word)
print("Number of occurrences of '{}' in the string: {}".format(search_word, occurrence_count))
