import pandas as pd
import numpy as np

data = {
    'Математика' : [4, 5, 4, 5, 4, 3, 5, 3, 5, 3],
    'Русский язык' :[5, 5, 5, 5, 5, 4, 3, 5, 2, 3],
    'Физика' : [4, 5, 4, 5, 5, 4, 3, 5, 2, 5],
    'Химия' : [5, 4, 3, 5, 2, 5, 4, 5, 5, 5],
    'Физкультура' : [4, 3, 5, 2, 5, 4, 3, 5, 2, 3]
}

df = pd. DataFrame(data)
print(df.describe())


Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
print(f"IQR Математика = {IQR_math}")

Q1_rus= df['Русский язык'].quantile(0.25)
Q3_rus = df['Русский язык'].quantile(0.75)
IQR_rus = Q3_rus - Q1_rus
print(f"IQR Русский язык = {IQR_rus}")

Q1_fiz = df['Физика'].quantile(0.25)
Q3_fiz= df['Физика'].quantile(0.75)
IQR_fiz= Q3_fiz - Q1_fiz
print(f"IQR Физика= {IQR_fiz}")

Q1_him = df['Химия'].quantile(0.25)
Q3_him = df['Химия'].quantile(0.75)
IQR_him= Q3_him - Q1_him
print(f"IQR Химия = {IQR_him}")

Q1_fizk = df['Физкультура'].quantile(0.25)
Q3_fizk = df['Физкультура'].quantile(0.75)
IQR_fizk= Q3_fizk - Q1_fizk
print(f"IQR Физкультура= {IQR_fizk}")





print(f"Средняя оценка Математика - {df['Математика'].mean()}")
print(f"Средняя оценка Русский язык - {df['Русский язык'].mean()}")
print(f"Средняя оценка Физика - {df['Физика'].mean()}")
print(f"Средняя оценка Математика - {df['Математика'].mean()}")
print(f"Средняя оценка Физкультура - {df['Физкультура'].mean()}")


print(f"Медианная оценка Математика- {df['Математика'].median()}")
print(f"Медианная оценка Русский язык- {df['Русский язык'].median()}")
print(f"Медианная оценка Физика- {df['Физика'].median()}")
print(f"Медианная оценка Математика- {df['Математика'].median()}")
print(f"Медианная оценка Физкультура- {df['Физкультура'].median()}")


print(f"Стандартное отклонение Математика- {df['Математика'].std()}")
print(f"Стандартное отклонениеРусский язык- {df['Русский язык'].std()}")
print(f"Стандартное отклонение Русский язык- {df['Русский язык'].std()}")
print(f"Стандартное отклонение Русский язык- {df['Русский язык'].std()}")
print(f"Стандартное отклонение Русский язык- {df['Русский язык'].std()}")



print(df.describe())


