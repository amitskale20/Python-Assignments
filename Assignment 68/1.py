##########################################################
#
#    Manual Convolution Program
#
##########################################################

def main():

    # Define 5x5 input grayscale image
    image = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    # Define 3x3 edge detection kernel
    kernel = [
        [-1, -1, -1],
        [0, 0, 0],
        [1, 1, 1]
    ]

    # Get image and kernel size
    img_height = len(image)
    img_width = len(image[0])
    kernel_size = len(kernel)

    # Store feature map
    feature_map = []

    # Slide kernel over image
    for i in range(img_height - kernel_size + 1):

        feature_row = []

        for j in range(img_width - kernel_size + 1):

            # Extract region
            region = [
                row[j:j + kernel_size]
                for row in image[i:i + kernel_size]
            ]

            # Calculate convolution
            conv_sum = 0

            for r in range(kernel_size):
                for c in range(kernel_size):
                    conv_sum += region[r][c] * kernel[r][c]

            feature_row.append(conv_sum)

        feature_map.append(feature_row)

    # Display feature map
    print("Feature Map Output :")

    for row in feature_map:
        print(row)


if __name__ == "__main__":
    main()