import cv2
print("this program makes a meme with text ontop of a picture")

# Read the image file

picture = cv2.imread('cat.jpg')

# Add text ontop of cat.jpg
                                                # Coordinates
cv2.putText(picture, "This is working properly", (10,100),
    cv2.FONT_HERSHEY_SIMPLEX, .75, (255,255,0) , 4)
                     # FONT SIZE,   COLOR,    THICKNESS
#Show the picture with the added text

cv2.imshow('Meme' , picture)
#Record the waitkey preessed by user and create a new variable
keypressed = cv2.waitKey(0)


while keypressed != 27:
    print('invalid key',keypressed)
    keypressed = cv2.waitKey(0)

#Now only way to do this is if user presses esc
cv2.destroyAllWindows()