students = {
"101": {"name": "Rahul", "age": 21, "city": "Delhi"},
"102": {"name": "Priya", "age": 20, "city": "Mumbai"},
"103": {"name": "Karan", "age": 22, "city": "Pune"}
}

for roll, details in students.items():
     print(roll, details) #    returns every key-value pair
    # print(roll, details['name'])  #    returns only names from the values as explicitly mentioned
    # print(roll, details['name'], details['city'])  #    returns both names, cities from the values as explicitly mentioned

#   to find age total we can as
total = 0
for roll, details in students.items():
    total += details['age']
print(f'age total is : {total}')