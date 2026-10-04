##########################################################
#
#    Flattening and Fully Connected Layer Program
#
##########################################################

def main():

    # Take a 2D matrix
    matrix = [
        [6, 4],
        [8, 6]
    ]

    print("Input Matrix :")

    for row in matrix:
        print(row)

    # Convert 2D matrix into 1D vector
    flatten_output = [
        element
        for row in matrix
        for element in row
    ]

    print("\nFlatten Output (1D Vector) :", flatten_output)

    # Define weights and bias
    weights = [0.2, 0.4, -0.5, 0.1]
    bias = 0.5

    # Calculate fully connected layer output
    manual_output = sum(
        f * w
        for f, w in zip(flatten_output, weights)
    ) + bias

    print(
        "Fully Connected Layer Manual Output :",
        manual_output
    )

    # Explain flattening
    print("\nExplanation:")

    print(
        "The flatten layer converts a multi-dimensional "
        "feature map into a one-dimensional vector. "
        "This vector is then passed to fully connected "
        "Dense layers for classification."
    )


if __name__ == "__main__":
    main()