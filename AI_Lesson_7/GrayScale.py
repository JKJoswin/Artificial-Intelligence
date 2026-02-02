import cv2

image = cv2.imread('example.jpg')

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resized = cv2.resize(gray,((224,224)))

cv2.imshow('Resized GrayScale Image', resized)
print("Press 's' key to save the image.")
key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite("output_224x224_gray.jpg",resized)
    print("Image Saved Successfully!")