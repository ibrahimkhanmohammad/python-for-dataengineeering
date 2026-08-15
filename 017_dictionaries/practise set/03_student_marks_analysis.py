#   Design a dictionary where each key is a student's name and the corresponding value is a list of their marks in 3 different subjects. Calculate and print the total marks and average marks for each student


details = {
    'asta': [8, 6, 6],
    'yami': [9, 8, 6],
    'yuno': [9, 5, 5],
    'luck': [7, 7, 4]
}

for stud, marks in details.items():
    total = sum(marks)
    avg = total / len(marks)
    print(f"{stud}: Total = {total}, Average = {avg:.2f}")
