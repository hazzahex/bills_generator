import pandas as pd

keywords = ["MILK AND", "BT CONSUMER", "BRISTOL CC L TAX", "BRITISH GAS", "TV LICENCE", "WESSEXWATER", "MM RECUR"]
housemates = ["Elise", "Annabel", "Lizzy", "Harry"]

df = pd.read_csv('data/jan2022.csv')
df = df.drop("Number", axis=1)
df = df.drop("Account", axis=1)
df = df.drop("Subcategory", axis=1)

df = df[df.Memo.str.contains('|'.join(keywords))]
df["Each"] = df["Amount"] / len(housemates)

print(df)
print(f"Total Bills = {0 - df['Amount'].sum()}")
print(f"Each = {0 - df['Each'].sum()}")


