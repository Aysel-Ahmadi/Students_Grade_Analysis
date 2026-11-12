# Repository: https://github.com/Aysel-Ahmadi/Students_Grade_Analysis

import csv
students = []
with open("students.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
        if row["score"] == "score":
          continue
        student = {"name":row["name"],"score": float(row["score"])}

    
    students.append(student)
    average = sum(student["score"] for student in students) / len(students)

highest_score = max(student["score"] for student in students)
lowest_score = min(student["score"] for student in students)

failed_students = [student for student in students
    if student["score"] < 12]

top_students = [student for student in students
    if student["score"] > 17]

def get_score(student):
    return student["score"]

sorted_students = sorted(students, key=get_score, reverse=True)
with open("failed_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(failed_students)

    with open("top_students.csv", "w", newline="") as file:
      writer = csv.DictWriter(file, fieldnames=["name", "score"])
      writer.writeheader()
      writer.writerows(top_students)

    with open("sorted_students.csv", "w", newline="") as file:
     writer = csv.DictWriter(file, fieldnames=["name", "score"])
     writer.writeheader()
     writer.writerows(sorted_students)
    lowest_students = []

for student in students:
    if student["score"] == lowest_score:
        lowest_students.append(student)
        highest_students = []

lowest_students = []

for student in students:
    if student["score"] == lowest_score:
        lowest_students.append(student)

        print("Average:", average)
print("Highest score:", highest_score)

for student in highest_students:
    print(student["name"])

print("Lowest score:", lowest_score)

for student in lowest_students:
    print(student["name"])

print("Failed count:", len(failed_students))
print("Top count:", len(top_students))