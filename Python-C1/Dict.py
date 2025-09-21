n = int(input("Enter number of customer: "))
customer_product= {}

for i in range(n+1):
    name = input("Enter a name")
    product = input("Enter product name:")
    customer_product[name] = product

product_customer ={}

for customer, product in customer_product.items():
    if product not in product_customer:
        product_customer[product] = []
    product_customer[product].append(customer)

print("Final Dictionary")
for product, customer in product_customer.items():
    print(f"{product}: {customer}")
