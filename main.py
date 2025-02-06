import pandas as pd

# Keywords to identify bills
keywords = ["MILK AND", "BT CONSUMER", "BRISTOL CC L TAX",
            "BRITISH GAS", "TV LICENCE", "WESSEXWATER", "MM RECUR", "BT GROUP PLC"]

# Housemates list
housemates = ["Annabel", "Arty", "Pippa", "Alex"]


def horizontal_rule():
    print("----------------------------------------")


def main():
    # Collect days each housemate has been in the house this month
    portions = []
    for housemate in housemates:
        portions.append(
            int(input(f"How many days has {housemate} been in the house this month? ")))

    total_housemate_days = sum(portions)
    horizontal_rule()
    print(f"Dividing bills by {total_housemate_days} days...")

    # Read bills data from CSV
    df = pd.read_csv('data/jan2025.csv', encoding="ISO-8859-1")

    # Filter bills based on keywords
    df = df[df['Memo'].str.contains('|'.join(keywords))]

    # Remove specific bill entry
    df = df[~df['Memo'].str.contains("BRITISH GAS SERVIC")]

    # Calculate micro portion for each bill
    df["Micro"] = df["Amount"] / total_housemate_days

    total_micro = -df["Micro"].sum()
    horizontal_rule()
    print("Bills table:")

    thin_table = df.drop(["Number", "Account", "Subcategory"], axis=1)
    thin_table['Memo'] = thin_table['Memo'].str.strip().str.split(r'\\|\t').str[0].str.strip()

    print(thin_table)
    horizontal_rule()
    print("Housemate breakdown...")

    # Distribute bills among housemates
    for housemate, portion in zip(housemates, portions):
        total = total_micro * portion
        amount_string = '£{:.2f}'.format(total)
        print(f"{housemate} - {amount_string}")


if __name__ == "__main__":
    main()
