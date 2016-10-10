word = input("Type a word: ")
i = len(word)
vowels = word[1::2]
k = 0
if vowels[1] == 'а' or vowels[1] == 'е' or vowels[1] == 'и' or vowels[1] == 'о' or vowels[1] == 'у' or vowels[1] == 'ы' or vowels[1] == 'э' or vowels[1] == 'я' or vowels[1] == 'ю':
    for letter in vowels:
        if letter == vowels[1]:
            k += 1
if k == len(vowels) and len(word) % 2 == 0:
    print("It is banana-language!!!")
else:
    print("I don't know that language...")
