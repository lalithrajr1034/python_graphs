import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_A_sales = [100, 120, 130, 150, 160, 180]
product_B_sales = [80, 100, 90, 110, 120, 130]
product_C_sales = [60, 70, 60, 80, 90, 100]

plt.plot(months, product_A_sales, label='Product A')
plt.plot(months, product_B_sales, label='Product B')
plt.plot(months, product_C_sales, label='Product C')

plt.title('Sales Comparison (Subplot)')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
