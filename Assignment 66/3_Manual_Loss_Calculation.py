##########################################################
#
#   Loss Functions
#
##########################################################

import math


def MeanSquaredError(actual, predicted):

    loss = 0

    for i in range(len(actual)):

        loss = loss + (
            (actual[i] - predicted[i]) ** 2
        )

    loss = loss / len(actual)

    return loss


def BinaryCrossEntropy(actual, predicted):

    loss = 0

    for i in range(len(actual)):

        loss = loss + (
            actual[i] * math.log(predicted[i])
            +
            (1 - actual[i]) * math.log(1 - predicted[i])
        )

    loss = -loss / len(actual)

    return loss


def main():

    actual = [
        1,
        0,
        1,
        1
    ]

    predicted = [
        0.9,
        0.2,
        0.8,
        0.7
    ]

    mse = MeanSquaredError(
        actual,
        predicted
    )

    bce = BinaryCrossEntropy(
        actual,
        predicted
    )

    print("Mean Squared Error :", mse)

    print("Binary Cross Entropy :", bce)


if __name__ == "__main__":
    main()