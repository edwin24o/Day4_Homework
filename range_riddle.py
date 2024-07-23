days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#Task1

for days_even in range(len(days_of_week)):
    if days_even % 2 == 0:
        print(days_of_week[days_even])