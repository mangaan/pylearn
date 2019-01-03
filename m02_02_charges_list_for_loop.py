balance = 1000.00
name = "Chuck Black"
account_no = "01123581321"

print("name:", name, "      account:", account_no, "                     original balance:", "$" + str(balance))

charges = [5.99, 12.45, 28.05, 2.34, 4.56, 6.78, 8.90]

for charge in charges:
    balance = balance - charge
    print("name:", name, "      account:", account_no, "    charge:", charge, "     new balance:",  "$" + str(balance))



