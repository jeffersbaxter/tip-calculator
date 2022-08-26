print("Welcome to the tip calculator.")

total = input("What was the total bill?\n")

if total[0] == "$":
  total = total[1:]

total_as_float = float(total)

tip_perc = float(input("What percentage tip would you like to give? 10, 12, or 15?\n")) / 100

num_of_people = int(input("How many people to split the bill?\n"))

bill_per_person = "{:.2f}".format(total_as_float * (1 + tip_perc) / num_of_people)

print(f"Each person should pay: ${bill_per_person}")
