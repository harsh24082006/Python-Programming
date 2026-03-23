def char_frequency(text):
    freq_dict = {}
    for char in text:
        # Increment the count if character exists, else initialize to 1
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

# Example usage
string = "hello world"
result = char_frequency(string)
print("Character frequencies:", result)