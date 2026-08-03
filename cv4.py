import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\DeLL\OneDrive\Documents\python\Screenshot 2026-07-16 115114.png")

if image is None:
    print("Error: Image not found!")
else:
    # Create a 5x5 kernel
    kernel = np.ones((5,5), np.uint8)

    # Dilate the image
    dilated_image = cv2.dilate(image, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
