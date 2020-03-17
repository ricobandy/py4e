user_hrs = float(input("Enter Hours: "))
rate_per_hour = float(input("Enter Rate: "))

if user_hrs <= 40:
	pay = user_hrs * rate_per_hour
else:
	pay = (40 * rate_per_hour) + ((user_hrs - 40) * 1.5 * rate_per_hour)

print("Pay:", pay)
