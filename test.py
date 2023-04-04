from libpy import text_utils

filename = "config.txt"
num_words = text_utils.count_words(filename=filename)

if num_words is not None:
    print(f"The file {filename} has {num_words} words.")
else:
    print(f"Error: file {filename} not founded.")
