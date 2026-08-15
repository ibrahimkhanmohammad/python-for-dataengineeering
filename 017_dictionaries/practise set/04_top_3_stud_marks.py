#   Given a dictionary of subjects and their marks, sort it by marks in descending order. Then, print only the top 3 subjects with the highest marks

subjects = {
    "Mathematics": 88,
    "Science": 95,
    "English": 72,
    "History": 80,
    "Geography": 67,
    "Computer": 91,
}

ans = sorted(subjects.items(), key=lambda x: x[1], reverse=True)
result = ans[:3]
for sub, mark in result:
    print(f"{sub} = {mark}")