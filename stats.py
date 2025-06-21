def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_nums(text):
    lower_char = text.lower()
    char_counts = {}
    for char in lower_char:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char(char_counts):
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=lambda item: item["num"])
    return char_list