import cv2

# Load image
image = cv2.imread('images/3.jpg')

if image is None:
    print("Error: Could not load image. Please check the file path.")
else:
    # Apply Gaussian Blur
    gaussian = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply Median Blur
    median = cv2.medianBlur(image, 5)

    # Show results
    cv2.imshow('Original Image', image)
    cv2.imshow('Gaussian Blur', gaussian)
    cv2.imshow('Median Blur', median)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
