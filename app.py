import cv2
import numpy as np

# Define the image size
width, height = 500,500 

# Create an all-white image
image = np.zeros((height, width), dtype=np.uint8) * 255

# Create a black rectangle (you can customize the shape)
cv2.rectangle(image, (20, 20), (80, 80), 255, thickness=-1)

# Save the image
cv2.imwrite('simple_bw_image.png', image)

# Display the image (optional)
cv2.imshow('Simple Black and White Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
