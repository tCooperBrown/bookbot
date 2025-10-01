def get_num_words(text):
    return len(text.split())

def get_instances_of_chars(text):
    lower_text = text.lower()
    instances_dict = {}

    for char in lower_text:
        if not instances_dict.get(char):
            instances_dict[char] = 0
        
        instances_dict[char] += 1

    return instances_dict

def sort_on(dictionary):
    return dictionary["num"]

def get_sorted_list_of_dict(dictionary):
    list_of_char_dicts = []
    
    for (key, value) in dictionary.items():
        list_of_char_dicts.append({"char": key, "num": value})
    
    return sorted(list_of_char_dicts, key=sort_on, reverse=True)




