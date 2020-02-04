sentence = input("Please Enter any sentence  ")
print(sentence)

words = sentence.split()

print(words)

long_word_length = len(words[0])

for i in words:
    word_length=len(i)
    if word_length>long_word_length:
        long_word_length = word_length
        currentword=i
print("Longest word is:" ,currentword)
print("Length is:",long_word_length)        