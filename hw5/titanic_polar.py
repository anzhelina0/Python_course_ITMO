import polars as pl
import bottleneck as bn
import pandas as pd

# Считайте датасет из файла train.csv (это данные о выживаемости на Титанике) с помощью polars
df = pl.read_csv("hw5/titanic.csv")

# Выведите основную информацию о датасете: информацию о типах данных, число пропусков, средние значения и т.д
print(df.dtypes)
print(df.null_count())
print(df.mean())

# Посчитайте количество пассажиров каждого класса (Pclass)
print(df.get_column("Pclass").value_counts())

# Выведите количество выживших мужчин и женщин на корабле
survived_counts = df.group_by("Sex").agg(pl.col("Survived").sum())
print(survived_counts)

# Выведите часть таблицы с пассажирами, возраст которых больше 44 лет
print(df.filter(pl.col("Age")>44))

# Посчитайте средний возраст пассажиров и его стандартное отклонение с помощью bottleneck
print(bn.nanmean(df.get_column("Age")))
print(bn.nanstd(df.get_column("Age")))
# Для каждого пассажира умножьте значение столбца Fare на 1.3 и сохраните результаты как новый столбец Fare_new
df_2 = pd.read_csv("hw5/titanic.csv")
df_2["Fare_new"] = df_2["Fare"].apply(lambda x: x*1.3)

# Считайте датасет из файла Housing.csv (это данные о ценах домов) с помощью pandas
df_housing = pd.read_csv("hw5/Housing.csv")

df_housing.info()
# Можно заменить все int64 на int32 или int8 в зависимости от назначения столбца, чтобы уменьшить размер данных + ввести булевый тип для столбцов со значениями yes\no
yes_no = ["mainroad", "guestroom", "basement", "hotwaterheating", "airconditioning"]
df_housing[yes_no] = df_housing[yes_no].replace({"yes": True, "no": False})
df_housing = df_housing.astype({"price": "int32", "area": "int32", "bedrooms": "int8", "bathrooms": "int8", "stories": "int8"})
df_housing.info()