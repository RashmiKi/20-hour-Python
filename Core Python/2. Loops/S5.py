name = input("Enter your name: ")


for i in name:
    c=0
    for j in name:
        if i==j:
            c = c+1
    if c==1:
      print("The first non-repeated character,", i)
      break