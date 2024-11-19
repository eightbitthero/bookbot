def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = count(text)
    letter_count = char_count(text)
    sorted_letter_list = chars_dict_to_sorted_list(letter_count) 
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document")
    for sorted_output in sorted_letter_list:
        if sorted_output["char"].isalpha():
            print(f"The '{sorted_output["char"]}' character was found {sorted_output["num"]} times " )
   



def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count(doc):
    words = doc.split()
    return(len(words))

def char_count(fulltext):
    letter_count = {}
    loweredtext = fulltext.lower()
    for lower in loweredtext:
        letter_count[lower] = 0
    for lower in loweredtext:
        letter_count[lower] += 1
    return letter_count

def letter_sort(val):
    return val["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char":ch,"num":num_chars_dict[ch]})
    sorted_list.sort(reverse=True,key= letter_sort)
    return sorted_list
main()