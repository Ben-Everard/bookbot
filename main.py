def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read();

    lower_case = file_contents.lower()

    report(lower_case)

def word_count(file):
    word_array = file.split()

    return len(word_array)

def letter_count(file):
    characters = {}
    
    for i in file:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1

    return characters

def dict_to_list(dict):
    list_char = dict.items() 
    alpha = []
    for char in list_char:
        if char[0].isalpha():
            alpha.append(char)

    return alpha

def sort_on(item):
    return item[1]

def make_report(word_count, sort_char):
    report = ''
    report += "--- Report for Frankenstien ---\n"
    report += f"{word_count} words found in the document\n\n"

    for char in sort_char:
        report += f"The '{char[0]}' character was found {char[1]} times\n"

    report += "--- End report ---"
    return report

def report(book):
    count = word_count(book)
    chars = letter_count(book)

    char_list = dict_to_list(chars)
    char_list.sort(reverse=True, key=sort_on)

    full_report  = make_report(count, char_list)
    print(full_report)

main()

