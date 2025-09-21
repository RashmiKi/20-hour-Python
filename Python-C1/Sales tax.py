product_price = float (input("Enter price of the product: "))
discount = float (input("Enter the discount for the product: "))
sales_tax = float (input("Enter sales tax on product: "))

selling_price = product_price - (discount*product_price) + (sales_tax*product_price)
print ("Selling price of Product:", selling_price)