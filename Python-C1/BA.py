def categorize_customer(name,spending):
    if spending>=100000:
        value = "High Value"
    elif spending>=50000 and spending<100000:
       value = "Medium Value"
    else:
        value = "Low Value"
    return value

limit = int(input("Enter the limit of the customer: "))

for i in range(1,limit+1):
    cust_name = input("Enter customer Name: ")
    cust_spending = int(input("Enter your spending: "))
    actual= categorize_customer(cust_name, cust_spending)
    print("Name:", cust_name)
    print("Value: ", actual)

    

        