import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("hw4\itanic.csv")

# Визуализируйте распределение значений признаков Survived, Pclass, Age, Sex. Parch 

# Survived
df_surv = df['Survived'].value_counts().dropna()
labels = 'Survived', 'Died'
fig, ax0 = plt.subplots()
ax0.set_title('Процент выживших')
ax0.pie(df_surv, labels=labels, autopct='%1.1f%%')

# Pclass
df_pcl = df['Pclass'].value_counts().sort_index()
labels = 'class_first', 'class_second', 'class_third'
fig, ax1 = plt.subplots()
ax1.set_title('Распределение классов кабин')
ax1.pie(df_pcl, labels=labels, autopct='%1.1f%%')


# Age
df_age = df['Age'].dropna()
fig, ax2 = plt.subplots()
sns.boxplot(df_age)
ax2.set_title('Возраст пассажиров')
plt.show()

## Пояснения: на графике виден сред

# Sex
df_sx = df['Sex'].value_counts().sort_index()
labels = 'male', 'female'
fig, ax3 = plt.subplots()
ax3.set_title('Пол пассажиров')
ax3.pie(df_sx, labels=labels, autopct='%1.1f%%')


# Parch 
df_prch = df['Parch'].value_counts().sort_index()
fig, ax4 = plt.subplots()

ax4.bar(df_prch.index, df_prch.values)

ax4.set_title('Наличие родителей или детей на борту')
ax4.set_xlabel('Количество родителей или детей')
ax4.set_ylabel('У скольких пассажиров')

plt.show()