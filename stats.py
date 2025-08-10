def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text): 
	count_char = {}
	for char in text:
		lowered_char = char.lower()
		if lowered_char in count_char: 
			count_char [lowered_char] += 1 
		else: 
			count_char[lowered_char] = 1
	return count_char

def sort_characters(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # Ignora caracteres não alfabéticos
            sorted_list.append({"char": char, "num": count})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
