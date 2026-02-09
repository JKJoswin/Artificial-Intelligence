import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title,image):
    plt.figure(figsize = (8,8))
    if len(image.shape) == 2:
        plt.imshow(image,cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    image = cv2.imread(image_path)
    if image == None:
        print('Error: Image not found!')
        return
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    display_image("Original Grayscale Image",gray_image)

    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Guassian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")

    while True:
        choice = input('Enter your choice (1-6):')

        if choice == 1:
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
            display_image("Sobel Edge Detection",combined_sobel)