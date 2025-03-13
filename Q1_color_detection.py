import cv2
import numpy as np

# Load image
image = cv2.imread('images/1.jpg')

# Convert to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define color range (example: Red color)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

# Create mask
mask = cv2.inRange(hsv, lower_red, upper_red)

# Extract the detected color
result = cv2.bitwise_and(image, image, mask=mask)

# Show results
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
