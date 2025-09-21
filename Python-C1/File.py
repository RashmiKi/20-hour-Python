file = open(r"D:\Python\20-hour-Python\Python-C1\practice.txt", mode= "r")
data = file.read()
print(data)
newdata = data.replace("Java","Python")
print(newdata)
if "learning" in data:
    print("Word Found")
else:
    print("Not Found")
file.close()
file = open(r"D:\Python\20-hour-Python\Python-C1\practice.txt",mode = "w")
file.write(newdata)
file.close()