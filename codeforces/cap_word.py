"""
Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.

Input
A single line contains a non-empty word. This word consists of lowercase and uppercase English letters.
The length of the word will not exceed 103.

Output the given word after capitalization.
"""


def capitalize_word(word: str):
    if not word:
        return None
    if word[0].isalpha():
        fc = word[0].capitalize()

    return fc+word[1:]


if __name__ == "__main__":
    word = input()
    print(capitalize_word(word))
