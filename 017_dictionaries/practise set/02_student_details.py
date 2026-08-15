#   Create a nested dictionary containing details for 4 students, where each student entry includes their name, age, and city. Write a loop to print the full details of each student in a clear, readable format.

details = {
            '101': {'name': 'abc', 'age': 89, 'city': 'cid'},
            '102': {'name': 'xyz', 'age': 98, 'city': 'ias'},
            '103': {'name': 'pqr', 'age': 100, 'city': 'ssc'},
            '104': {'name': 'mno', 'age': 85, 'city': 'iit'},
          }

for id, detail in details.items():
    print(f'student id : {id}')
    print(f'student name : {detail['name']}')
    print(f'student age : {detail['age']}')
    print(f'student city : {detail['city']}')
    print()