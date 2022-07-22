# we can use or mention the {0} index value of that variable number to be sure that arguement was placed in the correct placeholder.


quantity = 3        # quantity is nothing but pieces
itemno = 567         # items or number of items
price = 49.95        # the price of the dollars


myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# here in function print() the format alignment is not changed but in the order itself added the index{0},{1} & {2} as per the placeholder.