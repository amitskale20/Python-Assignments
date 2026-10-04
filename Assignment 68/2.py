##########################################################
#
#    ReLU and Max Pooling Program
#
##########################################################

def main():

    # Create feature map
    feature_map = [
        [3, 3, 3],
        [0, 0, 0],
        [-3, -3, -3]
    ]

    print("Input Feature Map :")

    for row in feature_map:
        print(row)

    # Apply ReLU
    # Negative values become 0
    # Positive values remain unchanged

    relu_output = []

    for row in feature_map:
        relu_row = [max(0, val) for val in row]
        relu_output.append(relu_row)

    print("\nReLU Output :")

    for row in relu_output:
        print(row)

    # Apply 2x2 Max Pooling

    pooled_output = [
        [
            max(
                relu_output[0][0],
                relu_output[0][1],
                relu_output[1][0],
                relu_output[1][1]
            ),

            max(
                relu_output[0][1],
                relu_output[0][2],
                relu_output[1][1],
                relu_output[1][2]
            )
        ],

        [
            max(
                relu_output[1][0],
                relu_output[1][1],
                relu_output[2][0],
                relu_output[2][1]
            ),

            max(
                relu_output[1][1],
                relu_output[1][2],
                relu_output[2][1],
                relu_output[2][2]
            )
        ]
    ]

    print("\n2x2 Max Pooling Output :")

    for row in pooled_output:
        print(row)

    # Explanation

    print("\nExplanation:")
    print(
        "Pooling reduces spatial dimensions by extracting "
        "the maximum value from local regions."
    )


if __name__ == "__main__":
    main()