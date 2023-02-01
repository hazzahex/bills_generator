import pandas as pd

keywords = ["MILK AND", "BT CONSUMER", "BRISTOL CC L TAX",
            "BRITISH GAS", "TV LICENCE", "WESSEXWATER", "MM RECUR"]
housemates = ["Annabel", "Harry", "Arty", "Bex", "Elise"]

portions = []


def horizontal_rule():
    print()
    print('----------------------------------------')
    print()


for housemate in housemates:
    portions.append(int(input("How many days has " +
                    housemate + " been in the house this month? ")))

total_housemate_days = sum(portions)
horizontal_rule()
print(f"Dividing bills by {total_housemate_days} days...")

df = pd.read_csv('data/jan2023.csv',
                 encoding="ISO-8859-1").drop(["Number", "Account", "Subcategory"], axis=1)

df = df[df.Memo.str.contains('|'.join(keywords))]
df["Micro"] = df["Amount"] / total_housemate_days
total_micro = 0 - df["Micro"].sum()
horizontal_rule()
print(f"Bills table:")
print(df)
horizontal_rule()
print(f"Housemate breakdown...")
for index, housemate in enumerate(housemates):
    total = total_micro * portions[index]
    amount_string = '£{:.2f}'.format(total)
    print(f"{housemate} - {amount_string}")
