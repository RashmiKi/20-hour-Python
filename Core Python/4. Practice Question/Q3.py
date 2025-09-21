#aaabb = a3b2

word = input("Enter a word: ")
freq= {}

for i in word:
    con = word.count(i)
    freq[i] = con

print(freq)
compressed = ""

for key,value in freq.items():
    compressed = compressed+ key+ str(value)

print(compressed)
