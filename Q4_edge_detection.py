import cv2

# Load image in grayscale
image = cv2.imread('images/4.jpg', 0)

# Apply Sobel Edge Detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# Apply Canny Edge Detection
canny = cv2.Canny(image, 100, 200)

# Show results
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Canny Edge Detection', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
