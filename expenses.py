expenses = []
num_of_expenses = int(input("Enter # of expenses:\n"))

for i in range(num_of_expenses):
   expenses.append(float(input("Enter amount spent on lunch for each day of the week:\n")))

total = sum(expenses)

print("You spent $", total, " on lunch this week", sep="")