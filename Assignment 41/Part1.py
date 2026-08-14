import math
 
# Dataset
data = [
    ("A", 1, 2, "Red"),
    ("B", 2, 3, "Red"),
    ("C", 3, 1, "Blue"),
    ("D", 6, 5, "Blue")
]
 
# Accept input
x_new = float(input("Enter X coordinate: "))
y_new = float(input("Enter Y coordinate: "))
 
# K value
K = 3
 
# Calculate distances
distances = []
 
for point, x, y, label in data:
 
    distance = math.sqrt(
        (x_new - x) ** 2 +
        (y_new - y) ** 2
    )
 
    distances.append(
        (point, distance, label)
    )
 
# Sort distances
distances.sort(key=lambda item: item[1])
 
# Select K nearest neighbors
nearest = distances[:K]
 
# Display neighbors
print("\nNearest Neighbors:")
 
for point, distance, label in nearest:
    print(
        point,
        "- Distance:",
        round(distance, 2),
        "- Class:",
        label
    )
 
# Majority voting
votes = {}
 
for point, distance, label in nearest:
 
    if label not in votes:
        votes[label] = 0
 
    votes[label] += 1
 
# Find class with maximum votes
predicted_class = max(
    votes,
    key=votes.get
)
 
print("\nPredicted Class:", predicted_class)
 