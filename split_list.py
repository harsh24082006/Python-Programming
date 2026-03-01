# Accept user input
sentence = input("Enter a sentence: ")

# The split() method splits the string by spaces into a list of words
words_list = sentence.split()
word_count = len(words_list)

print("Sentence:", sentence)
print("Total number of words:", word_count)