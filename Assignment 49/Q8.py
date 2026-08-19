from sklearn.metrics import confusion_matrix

actual = [1, 1, 1, 1, 0, 0, 0, 0]

predicted = [1, 1, 0, 1, 0, 1, 0, 0]

# Calculate confusion matrix
cm = confusion_matrix(actual, predicted)

print("Confusion Matrix:")
print(cm)

# Extract values
TN, FP, FN, TP = cm.ravel()

print("True Positive (TP):", TP)
print("True Negative (TN):", TN)
print("False Positive (FP):", FP)
print("False Negative (FN):", FN)