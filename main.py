def count_words(text):
    # Split the text into words by whitespace and return the length of the resulting list
    words = text.split()
    return len(words)

def count_characters(text):
    # Split text into characters, remove duplicates, and return a dictionary with a key that represents the character and a frequency value
    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Loop through each character in the text
    for char in text:
        # Convert the character to lowercase
        char = char.lower()

        # If the character is already in the dictionary, increment its count
        if char in char_count:
            char_count[char] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            char_count[char] = 1

    return char_count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)

        # Call count_characters() to count the characters in the text
        character_counts = count_characters(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")

        # Call count_words() to count the words in the text
        word_count = count_words(file_contents)
        print(f"{word_count} words found in the document\n")

        # Sort the dictionary by character counts in descending order
        sorted_counts = sorted(character_counts.items(), key=lambda x: x[1], reverse=True)

        for char, count in sorted_counts:
            if char.isalpha():
                print(f"The '{char}' character was found {count} times")

        print("--- End Report ---")

main()