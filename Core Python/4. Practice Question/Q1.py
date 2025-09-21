username = input("Enter the string: ")
freq = {}

for i in username:
    con = username.count(i)
    freq[i] = con

print(freq)

#key are unique in nature