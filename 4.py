print("Welcome to the tip calculator.")

bill = float(input("what was the total bill? $ "))

tip = float(input("what percentage tip would you like to give? 10, 12, or 15?"))

people_to_split = float(input("how many people to split the bill?"))

total_bill = tip / 100 * bill + bill


people_to_split_and_the_bill_total = round(total_bill / people_to_split,2)

people_to_split_and_the_bill_total = "{:.2f}".format(total_bill / people_to_split,2)

print("Each person should pay:" + str(people_to_split_and_the_bill_total))