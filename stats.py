def get_num_of_words(book):
    book_list = book.split()
    return len(book_list)

def get_num_of_characters(book_content):
    count = {}
    for char in book_content:
        char = char.lower()
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    