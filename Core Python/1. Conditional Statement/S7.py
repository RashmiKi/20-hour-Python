coffee_size = input("Enter your coffee size ")
expresso_shot = input ("Do you want extra expresso shot type Y for yes and N for No ")

if expresso_shot == "Y":
    print("your coffee order is", coffee_size ,"and you need an expresso shot")
else:
    print("your coffee order is", coffee_size)