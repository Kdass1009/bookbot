def get_word_count(text):
    wordList = text.split()
    wordcount = len(wordList)
    return wordcount


def get_char_count(text):
    lower = text.lower()
    char_count = {}
    for letter in lower:
        if letter in char_count and letter.isalpha():
            char_count[letter] += 1
        elif letter.isalpha():
            char_count[letter] = 1
    sorted_chars = sorted(char_count.items(), reverse=True, key= lambda kv: (kv[1],kv[0]))
    for k,v in sorted_chars:
        print(f'{k}: {v}')

