import cv2

# Read the image
image = cv2.imread(r"C:\Users\DeLL\OneDrive\Documents\python\Screenshot 2026-07-16 115114.png")

if image is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    canny_image = cv2.Canny(gray_image, 100, 200)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Canny Edge Image", canny_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
