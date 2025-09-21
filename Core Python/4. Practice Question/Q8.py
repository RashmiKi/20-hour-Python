start = int(input("Enter the starting range: "))
end = int(input("Enter ending range: "))

for i in range(start, end+1):
    con = 0
    for j in range(1, i+1):
        if i%j == 0:
            con = con+1
    
    if con ==2 :
        print(i)

