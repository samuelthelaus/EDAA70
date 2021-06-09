import os
import string

def read_words(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)

    ord_lista = []
    for line in open(filepath, encoding='utf-8'):
        ord_lista.extend(line.split())
    
    ord_lista = [word.strip(string.punctuation + string.whitespace).lower() for word in ord_lista]

    return ord_lista
        

def count_only(text, bra_ord):
    my_dict = {key: 0 for key in bra_ord}
    for word in text:
        if word in bra_ord:
            my_dict[word] += 1

    return my_dict


def count_all_except(text, kassa_ord):
    my_set = set(text)
    my_dict = {key: 0 for key in my_set if key not in kassa_ord}
    for word in text:
        if word not in kassa_ord:
            my_dict[word] += 1

    return my_dict


def sorted_hist(my_dict):
    my_list = []
    for key in my_dict.keys():
        my_list.append((my_dict[key], key))
    
    my_list.sort(reverse=True)

    return my_list


def filter_hist(my_dict, n):
    my_dict = {key: value for key, value in my_dict.items() if value >= n}

    return my_dict


nils_lista = read_words('nilsholg.txt')

landskap = set(read_words('landskap.txt'))

undantag = set(read_words('undantagsord.txt'))

my_dict = count_all_except(nils_lista, undantag)

#my_list = sorted_hist(my_dict)

my_dict = filter_hist(my_dict, 100)

print(my_dict)

