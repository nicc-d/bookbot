from stats import get_num_words
from stats import each_character_count
from stats import sort_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)#calls the get_book_text function which opens the file containing the book
                                                  #as a list
    letter_count = each_character_count(text)
    num_words = get_num_words(text)#using imported function from stats.py
    finished_list = sort_list(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in finished_list:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')
    print("============= END =============")
    print(sys.argv)

    
        
        #f"Found {num_words} total words, {finished_list}")#prints results to the console
    

def get_book_text(path):#Function opens the txt file and
    with open(path) as f:
        file = f.read()#stores the opened file in a variable

    return file#returns the variable with the opened file

main()
