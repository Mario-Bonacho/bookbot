def words_counter(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter

def letters_counter(text):
    mod_string = text.lower()
    letters_dic = {}

    for char in mod_string:
        if char in letters_dic:
            letters_dic[char] += 1
        else:
            letters_dic[char] = 1
    return letters_dic
