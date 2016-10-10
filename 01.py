word = input("Type word - ")
i = len(word)
word1 = ""
while i > 0:
    word1 = word1 + word[i - 1]
    i -= 1
print(word1)
