import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Dataset loaded successfully!")
df = pd.read_csv("placement_data_full_class.csv")
# Link to placement_data_full_class.csv: https://www.kaggle.com/datasets/barkhaverma/placement-data-full-class
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(df['Marks'], bins=10, color='blue', edgecolor='black')
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')

placed_counts = df['Placed'].value_counts()
plt.subplot(1, 2, 2)
plt.bar(placed_counts.index, placed_counts.values, color=['green', 'red'])
plt.title('Bar Chart of Placement Status')
plt.xlabel('Placement Status')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

sns.set(style="ticks")
g = sns.FacetGrid(df, col="Placed")
g.map(plt.hist, "Marks", bins=10, color="purple", edgecolor="black")
g.add_legend()
plt.show()

sns.pairplot(df, hue="Placed", diag_kind="kde", markers=["o", "s"], height=2.5)
plt.show()

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.fill_between(placed_counts.index, placed_counts.values, color='orange', alpha=0.5)
plt.title('Area Chart of Placement Status')
plt.xlabel('Placement Status')
plt.ylabel('Count')

plt.subplot(1, 2, 2)
plt.pie(placed_counts.values, labels=placed_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightcoral'], startangle=90)
plt.title('Pie Chart of Placement Status')

plt.tight_layout()
plt.show()
