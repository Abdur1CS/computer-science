# Q04(a)

import random

# Get input
product = str(input("write the product here: "))



# Generate a random number between 10 and 30 inclusive
ranNum = random.randint(10,30)
print(ranNum)



# Generate the product code - first three letters of product name and the random number
productList =  list(product)
productCode =(f"{''.join(productList[:3])}{ranNum}")




# Display the product code and the product name
print(productCode)
print(f"product name = {product} and the product code = {ranNum}")