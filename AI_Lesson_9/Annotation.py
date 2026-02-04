import cv2
import matplotlib.pyplot as plt

image = cv2.imread("example.jpg")
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

height, width, _ =image_rgb.shape
rect1_height, rect1_width = 150, 150
top_left1 = (20,20)
bottom_right1 = (top_left1[0] + rect1_width, top_left1[1] + rect1_height)
cv2.rectangle(image_rgb,top_left1,bottom_right1,(0,255,255),10)

rect2_height, rect2_width = 200, 150
top_left2 = (width - rect2_width - 20, height - rect2_height - 20)
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect2_height)
cv2.rectangle(image_rgb,top_left1,bottom_right1,(0,255,255),3)

center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_height // 2
center2_x = top_left2[0] + rect2_width // 2
center2_y = top_left2[1] + rect2_height // 2
cv2.circle(image_rgb,(center1_x,center1_y),50,(0,255,0),-1)
cv2.circle(image_rgb,(center2_x,center2_y),15,(255,0,0),-1)
cv2.line(image_rgb,(center1_x,center1_y),(center2_x,center2_y),(0,255,0),5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.puttext(image_rgb,'Region-1',(top_left1[0]+100,top_left1[1]+100),font,2,(255,255,255))