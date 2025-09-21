original_string = input("Enter a string: ")
old_word = input("Enter a word to replace: ")
new_word = input ("Enter word to be replace with: ")

repl = original_string. split(old_word)
print(repl)

# for i in range(len(repl)):
#     if repl[i] == old_word:
#         repl[i] == new_word
             
# sentence = "". join(repl)   
# print(sentence)

sentence = new_word.join(repl)
print(sentence)

## join adds a new word between two elements of the list