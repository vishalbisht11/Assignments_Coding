# Program to find frequency of each distinct word in a given text file, 'input.txt'
# Output is stored in the file, 'output.txt' in alphanumeric order in word,frequency format.

import re  # Regular Expression module


def main():
    document_text = open('input.txt', 'r')    # Accessing the text file, input.txt in read mode.
    text_string = document_text.read().lower()   # Reading from the input.txt file.
    frequency = {}
    match_pattern = re.findall(r'\b[0-9]+\b', text_string)       # Finding numbers in the file, input.txt
    match_pattern2 = re.findall(r'\b[1-z]{1,30}\b', text_string)  # Finding words in the file, input.txt

    for word in match_pattern:    # Counting frequencies of numbers in the file, input.txt
        count = frequency.get(word, 0)
        frequency[word] = count+1

    for word in match_pattern2:   # Counting frequencies of the words in the file, input.txt
        count = frequency.get(word, 0)
        frequency[word] = count+1

    frequency_list = frequency.keys()
    print(frequency_list)
    out = open('output.txt', 'w')   # Accessing the file, output.txt in the write mode.

    for words in sorted(frequency_list):   # sorted() is used to sort in alphabetically order by key.
        print(words+"," + str(frequency[words]))
        out.write(words+"," + str(frequency[words])+"\n")


if __name__ == "__main__":
    main()