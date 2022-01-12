# Get loan Details
amount_owed = float(input("How much money is owed on the Loan?\n")) #$50,000
apr = float(input("What is the apr?\n")) #3%
monthly_payment = float(input("What is your monthly Payment?\n")) #$1,000
months = int(input("How many months do you want to see results for?\n")) #24

# Dived apr by 100 to make in a percent, then divide by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):
   #  Add interest
   interest_paid = amount_owed * monthly_rate
   amount_owed = amount_owed + interest_paid

   if (amount_owed - monthly_payment < 0):
      print("The last paymnent is", amount_owed)
      print("You paid off the loan in", i+1, "months.")
      break

   # Make payment
   amount_owed = amount_owed - monthly_payment

   #Print the results after this month
   print("Paid", monthly_payment, "of which", interest_paid, "was interest", end=' ')
   print("Now", amount_owed, "is owed")