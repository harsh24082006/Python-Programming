sentence = "python is great and python is easy to learn"
print("Original Sentence:", sentence)

# Split the sentence into a list of words
words_list = sentence.split()

# Convert the list to a set to remove duplicates
unique_words_set = set(words_list)

# Join the words back together (Note: sets are unordered, so order will change)
unique_sentence = " ".join(unique_words_set)

print("Sentence with unique words:", unique_sentence)