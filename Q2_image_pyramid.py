import cv2

# Load image
image = cv2.imread('images/2.jpg')

# Generate pyramid
num_levels = 4  # Number of levels in the pyramid
pyramid = [image]

for i in range(num_levels):
    image = cv2.pyrDown(image)
    pyramid.append(image)

# Display pyramid images
for i, img in enumerate(pyramid):
    cv2.imshow(f'Pyramid Level {i}', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
