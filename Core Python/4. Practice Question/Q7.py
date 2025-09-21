def frequency(word):
    freq = {}
    for i in word:
        con = word.count(i)
        freq[i] = con
    return freq

word1 = input("Enter a word: ")
word2 = input("Enter second word: ")

dictionary1 = frequency(word1)
dictionary2 = frequency(word2)

if dictionary1 == dictionary2:
    print("Anagram String")
else:
    print("Not an Anagram String")
