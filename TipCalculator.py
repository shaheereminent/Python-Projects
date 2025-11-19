greeting = print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12 or 15? "))
split_amount = int(input("How many people to split the bill? "))
bill_with_tip = tip_amount / 100 * total_bill + total_bill
each_person = bill_with_tip / split_amount 

print(f"Each person should pay: ${round(each_person, 2)} because with tip the bill is {bill_with_tip} and we're diving it with {split_amount}")

