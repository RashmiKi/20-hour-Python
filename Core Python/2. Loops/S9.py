duplicate_items = ["apple", "banana", "orange", "apple", "mango"]
count= 0

for i in duplicate_items:
    for j in duplicate_items:
        if i ==j:
            count = count +1
            
    if count ==2:
        print("The duplicate item is", i)
    break
