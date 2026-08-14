import math

Border = "=" * 50
 
# ==================================================
# PART 1
# KNN Classification for Points
# ==================================================
 
print(Border)
print("PART 1 - KNN CLASSIFICATION")
print(Border)
 
data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]
 
x_new = float(input("Enter X coordinate: "))
y_new = float(input("Enter Y coordinate: "))
 
K = 3
 
distances = []
 
for point, x, y, label in data:
 
    distance = math.sqrt(
        (x_new - x) ** 2 +
        (y_new - y) ** 2
    )
 
    distances.append(
        (point, distance, label)
    )
 
distances.sort(
    key=lambda item: item[1]
)
 
nearest = distances[:K]
 
print("\nNearest Neighbors:")
 
for point, distance, label in nearest:
 
    print(
        point,
        "- Distance:",
        round(distance, 2),
        "- Class:",
        label
    )
 
votes = {}
 
for point, distance, label in nearest:
 
    votes[label] = votes.get(label, 0) + 1
 
prediction = max(
    votes,
    key=votes.get
)
 
print("Predicted Class:", prediction)
 
 
# ==================================================
# PART 2
# Different K Values
# ==================================================
 
print(Border)
print("PART 2 - EFFECT OF K")
print(Border)
 
for K in [1, 3]:
 
    nearest = distances[:K]
 
    votes = {}
 
    for point, distance, label in nearest:
        votes[label] = votes.get(label, 0) + 1
 
    prediction = max(
        votes,
        key=votes.get
    )
 
    print(
        "K =", K,
        "->",
        prediction
    )
 
 
# ==================================================
# PART 3
# Student Pass/Fail
# ==================================================
 
print(Border)
print("PART 3 - STUDENT PERFORMANCE")
print(Border)
 
student_data = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]
 
study_hours = float(
    input("Enter Study Hours: ")
)
 
attendance = float(
    input("Enter Attendance: ")
)
 
K = 3
 
distances = []
 
for study, attend, result in student_data:
 
    distance = math.sqrt(
        (study_hours - study) ** 2 +
        (attendance - attend) ** 2
    )
 
    distances.append(
        (distance, result)
    )
 
distances.sort(
    key=lambda item: item[0]
)
 
nearest = distances[:K]
 
votes = {}
 
for distance, result in nearest:
 
    votes[result] = votes.get(result, 0) + 1
 
prediction = max(
    votes,
    key=votes.get
)
 
print("\nPredicted Result:", prediction)
 