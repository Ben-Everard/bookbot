def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read();


    word_count(file_contents)

def word_count(file):
    word_array = file.split()
    print(len(word_array))

main()
