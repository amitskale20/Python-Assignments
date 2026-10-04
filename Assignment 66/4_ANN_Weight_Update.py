##########################################################
#   4. Weight Update Using Gradient Descent
#   ANN Weight Update
#
##########################################################

def main():

    x = 2

    weight = 0.5

    bias = 0.2

    target = 1

    learning_rate = 0.1

    old_weight = weight

    prediction = (x * weight) + bias

    error = target - prediction

    weight = weight + (
        learning_rate * error * x
    )

    print("Input :", x)

    print("Old Weight :", old_weight)

    print("Bias :", bias)

    print("Target :", target)

    print("Prediction :", prediction)

    print("Error :", error)

    print("Updated Weight :", weight)


if __name__ == "__main__":
    main()