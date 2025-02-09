import seaborn as sns
import matplotlib.pyplot as plt

Programming=['Python', 'Java', 'C++', 'JavaScript', 'R'] 
Number= [55, 40, 35, 25, 15]

sns.set_theme(style="darkgrid") 
ax = sns.barplot(x=Programming,y=Number, palette="deep") 
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title("Programming Language Popularity Among Students")
plt.xlabel("Programming Language")
plt.ylabel("Number of Users")
plt.show()
