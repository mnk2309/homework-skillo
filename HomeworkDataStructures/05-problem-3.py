my_list = ["banana", "lemon", "Kawasaki", "ZiL", "demonstration", "iterate"]
otherList = [len(word) for word in my_list]

print(otherList)

wordLengthDict = {word: len(word) for word in my_list }
print(wordLengthDict)