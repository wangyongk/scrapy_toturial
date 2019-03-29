import pandas as pda

i=pda.read_csv(r"D:\Python\data\hexun.csv")
#i=i.describe()
i=i.sort_values(by="21")
print(i)