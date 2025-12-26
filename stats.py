def get_num_words(text):
    txt_string = text.split()
    count = 0
    for word in (txt_string):
        count += 1
    return count

def each_character_count(text):
    #txt_string = text.split()
    l_case_txt = text.lower()
    count_by_char = {}
    for letter in l_case_txt:
        if letter in count_by_char:
            count_by_char[letter] += 1
        else:
            count_by_char[letter] = 1  
    return count_by_char

def sort_on(x):
    return x["num"]

def sort_list(letter_count):
    list_of_dicts = []
    for char,count in letter_count.items():
        ind_dict = {}
        ind_dict["char"] = char
        ind_dict["num"] = count
        list_of_dicts.append(ind_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
        
    









        

