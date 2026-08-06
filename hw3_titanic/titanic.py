import pandas as pd

# чтение файла
df = pd.read_csv('hw3_titanic\itanic.csv')

# основная инф-я
df.info()
print(f"Средний возраст пассажиров: {df['Age'].mean()}")

# % выживаемости
print(df.groupby('Pclass')['Survived'].mean()*100)

# имя
df['first_name'] = df['Name'].apply(lambda x: x.split('.')[1].strip())
popular = (df.groupby('Sex')['first_name'].value_counts())

print(f"Популярное мужское имя: {popular['male'].idxmax()}")
print(f"Популярное женское имя: {popular['female'].idxmax()}")

# имя по классам
popular_2 = (df.groupby(['Sex','Pclass'])['first_name'].value_counts())

print(f"Популярное мужское имя в 1 классе: {popular_2['male', '1'].idxmax()}")
print(f"Популярное мужское имя в 2 классе: {popular_2['male', '2'].idxmax()}")
print(f"Популярное мужское имя в 3 классе: {popular_2['male', '3'].idxmax()}")
print(f"Популярное женское имя в 1 классе: {popular_2['female', '1'].idxmax()}")
print(f"Популярное женское имя в 2 классе: {popular_2['female', '2'].idxmax()}")
print(f"Популярное женское имя в 3 классе: {popular_2['female', '3'].idxmax()}")

# Выведите часть таблицы с пассажирами, возраст которых больше 44 лет
print(df[df['Age']>44])

# Выведите часть таблицы с пассажирами, возраст которых меньше 44 лет и которые мужского пола

print(df[(df['Age']<44) & (df['Sex'] == 'male')])

# Выведите количества n-местных кабин (в которых было 2, 3, 4, ... человека

cabins = df.groupby('Cabin')['PassengerId'].count()
print(cabins.value_counts())