import numpy as np
from sklearn.preprocessing import StandardScaler

data = np.array([
    [25, 20000],
    [30, 40000],
    [35, 80000]
])

# Points
point1 = data[0]
point2 = data[2]

# Distance before scaling
distance_before = np.linalg.norm(point1 - point2)

print("Distance Before Scaling:", distance_before)

# Apply scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

scaled_point1 = scaled_data[0]
scaled_point2 = scaled_data[2]

# Distance after scaling
distance_after = np.linalg.norm(
    scaled_point1 - scaled_point2
)

print("Distance After Scaling:", distance_after)