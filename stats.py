def word_counter(string):
    words = string.split()
    number = 0
    for i in range (0, len(words)):
        number += 1
    return number


def char_counter(string):
    chars = string[::1].lower()
    dictionary = {}
    for char in chars:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary
    

def sort_dict(dict):
    char_dict = sorted(
        [{"char": key, "count": value} for key, value in dict.items()],
        reverse=True,
        key=lambda item: item["count"]
    )
    return char_dict