text = ("As for my favorite part, it is the Council of Elrond. Man, in this chapter of the book, we dive into Middle "
        "Earth wholeheartedly. We learn about Elves, Dwarves, Humans, Beornings, enemies, etc. We catch up with "
        "Middle Earth as it is. Also, we go into the past and learn about many great things and people. Some parts "
        "are skipped, but it's nice to even imagine it. Then we meet many characters. That council atmosphere and "
        "manner of conversation are very appealing.")


def count_word_frequency(input_text):
    text = input_text.lower()

    words = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text).split()

    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency


result = count_word_frequency(text)

print(result)
