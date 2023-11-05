file = open("Alphabet.txt")
print(file.readlines())

word = input(f"Write a word: ").upper()
output_list = [file.letter for letter in word]
print(output_list)
