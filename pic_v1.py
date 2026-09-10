import cv2
print("this program will eventually make a meme with text ontop of a picture")
picture = cv2.imread('cat.jpg')

cv2.imshow('Meme' , picture)
cv2.waitKey(0)