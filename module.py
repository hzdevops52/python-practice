import random
import datetime

print(random.random())
print(random.randint(1,10))
print(random.randrange(1,100))
print(random.uniform(2.5,3.5))

cars = ['bmw', 'toyota', 'honda', 'suzuki']
print(random.choice(cars))

print(cars)
random.shuffle(cars)
print(cars)


#datetime
cur_date = datetime.datetime.now()
print(cur_date)

from datetime import datetime

# Let's say you have a date as a string
date_string = "2025-10-18"

# You need to convert it to a datetime object first using strptime()
# The format string '%Y-%m-%d' matches the format of your date_string
datetime_object = datetime.strptime(date_string, '%Y-%m-%d')

# Now you can use strftime() on the datetime_object
formatted_date = datetime_object.strftime('%A, %B %d, %Y')

print(f"Original string: {date_string}")
print(f"Formatted date: {formatted_date}")

