word = input("Type a word: ")
i = len(word)
vowels = word[1::2]
vow = "уеыаоэяию"
k = 0
if vowels[1] in vow:
    for letter in vowels:
        if letter == vowels[1]:
            k += 1
if k == len(vowels) and len(word) % 2 == 0:
    print("It is banana-language!!!")
else:
    print("I don't know that language...")
