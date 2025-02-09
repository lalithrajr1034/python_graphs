import matplotlib.pyplot as plt
product_A_sales = [100, 120, 130, 150, 160, 180]
plt.pie(product_A_sales,colors=['red','blue','green','yellow','orange','purple'],autopct='%1.1f%%')
plt.title("Sales of a product")
plt.show()