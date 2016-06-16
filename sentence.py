sentence = "Four score and seven years ago"

sentence_no_vowels = ""

for letter in sentence:
    if letter not in "AEIOUaeiou":
        sentence_no_vowels = sentence_no_vowels + letter 

print sentence_no_vowels