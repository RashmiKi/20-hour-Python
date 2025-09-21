def even_nums(limit):
    for i in range(2, limit+1):
        if i%2==0:
            yield i


lim = int(input("Enter a limit:  "))
ev = even_nums(lim)
for i in ev:
    print(i)