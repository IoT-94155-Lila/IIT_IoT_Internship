import datetime
current_datetime = datetime.datetime.now()

print("Current Date and Time:", current_datetime)

day_of_week = current_datetime.strftime("%A")
print("Day of the Week:", day_of_week)