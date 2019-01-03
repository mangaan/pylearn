balance = 1000.00
name = "Chuck Black"
account_no = "01123581321"

print("\nName:", name, "    account:", account_no, "     original balance:", "$" + str(balance))

print("\nName               Account          Charge     Balance")
for charge in open("m00_charges-only-file"):
    balance = balance - float(charge)
    print("{0:16}   {1:10}  {2:8,.3f}   {3:8,.3f}".format(name, account_no, float(charge), balance))
    
