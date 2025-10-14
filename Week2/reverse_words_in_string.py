# https://leetcode.com/problems/reverse-words-in-a-string/description/

def reverseWords(s):
    words = []
    word = ""

    for char in s:
        if char != ' ':
            word += char
        else:
            if word:
                words.append(word)
                word = ""

    if word:
        words.append(word)

    return ' '.join(reversed(words))
