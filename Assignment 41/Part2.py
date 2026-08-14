import math
 
# Student dataset
data = [
    (2, 60, "Fail"),
    (5, 80, "Pass"),
    (6, 85, "Pass"),
    (1, 50, "Fail")
]
 
# Accept input
study_hours = float(
    input("Enter Study Hours: ")
)
 
attendance = float(
    input("Enter Attendance: ")
)
 
# K value
K = 3
 
# Calculate distances
distances = []
 
for study, attend, result in data:
 
    distance = math.sqrt(
        (study_hours - study) ** 2 +
        (attendance - attend) ** 2
    )
 
    distances.append(
        (distance, result)
    )
 
# Sort distances
distances.sort(
    key=lambda item: item[0]
)
 
# Select K nearest neighbors
nearest = distances[:K]
 
# Display nearest neighbors
print("\nNearest Neighbors:")
 
for distance, result in nearest:
    print(
        "Distance:",
        round(distance, 2),
        "Result:",
        result
    )
 
# Majority voting
votes = {}
 
for distance, result in nearest:
 
    if result not in votes:
        votes[result] = 0
 
    votes[result] += 1
 
# Prediction
prediction = max(
    votes,
    key=votes.get
)
 
print("\nPredicted Result:", prediction)
 