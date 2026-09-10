import cv2
print("this program will eventually make a meme with text ontop of a picture")

# Read the image file

picture = cv2.imread('cat.jpg')

# Add text ontop of cat.jpg

cv2.putText(picture, "This is working properly", (10,100),
    cv2.FONT_HERSHEY_SIMPLEX, .75, (255,255,0) , 4)

#Show the picture with the added text

cv2.imshow('Meme' , picture)
cv2.waitKey(1)