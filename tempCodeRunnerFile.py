import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_A_sales = [100, 120, 130, 150, 160, 180]
product_B_sales = [80, 100, 90, 110, 120, 130]
product_C_sales = [60, 70, 60, 80, 90, 100]

fig,(ax11, ax2) = plt.subplots(1, 2)

ax11.stackplot(months, product_A_sales, product_B_sales, product_C_sales,labels=['Product A', 'Product B', 'Product C'])
ax11.set_title('Stacked Area Plot')
ax11.set_xlabel('Months')
ax11.set_ylabel('Sales')
ax11.legend()

ax2.plot(months, product_A_sales, label='Product A')
ax2.plot(months, product_B_sales, label='Product B')
ax2.plot(months, product_C_sales, label='Product C')

ax2.set_title('Sales Comparison (Subplot)')
ax2.set_xlabel('Months')
ax2.set_ylabel('Sales')
ax2.legend()
ax2.grid()

plt.tight_layout()
plt.show()