##########################################################
#
#   Activation Functions
#
##########################################################

import numpy as np
import matplotlib.pyplot as plt


def Sigmoid(x):

    return 1 / (1 + np.exp(-x))


def ReLU(x):

    return np.maximum(0, x)


def Tanh(x):

    return np.tanh(x)


def main():

    x = np.linspace(-10, 10, 100)

    sigmoid = Sigmoid(x)
    relu = ReLU(x)
    tanh = Tanh(x)

    plt.plot(
        x,
        sigmoid,
        label="Sigmoid"
    )

    plt.plot(
        x,
        relu,
        label="ReLU"
    )

    plt.plot(
        x,
        tanh,
        label="Tanh"
    )

    plt.xlabel("Input")

    plt.ylabel("Output")

    plt.title("Activation Functions")

    plt.legend()

    plt.grid()

    plt.show()


if __name__ == "__main__":
    main()