

def get_word_count(book_contents):
    num_words = len(book_contents.split())
    return num_words

def get_character_dict(book_contents):
    character_counter_dict = {}
    for letter in book_contents:
        letter_lower = letter.lower()
        
        if letter_lower not in character_counter_dict:
            character_counter_dict[letter_lower] = 1
        
        else: 
            character_counter_dict[letter_lower] += 1
    
    return character_counter_dict   

def sort_on(item):
    return item["num"]

def char_dict_to_sorted_list(char_dict):
    character_list = []
    for character in char_dict:
        character_list.append({"char": character,"num": char_dict[character]})
    character_list.sort(reverse = True, key = sort_on)
    return character_list

