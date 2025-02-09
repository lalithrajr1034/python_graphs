import matplotlib.pyplot as plt
product_A_sales = [100, 120, 130, 150, 160, 180]
product_sales=['jan','feb','mar','apr','may','jun']
plt.hist(product_A_sales, bins=5, edgecolor='black')
plt.title("Sales of a product")
plt.xlabel("Product A Sales")
plt.ylabel("Frequency")
plt.show()