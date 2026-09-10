'''
This program makes a meme with text on top of a picture. It allows the user to choose their own image, and write their own text on
top of this image. It also allows the user to change the color of text by pressing certain keys. Finally, it allows the user to save
their new custom image as a .jpg file.
Written by Ali Lalani
Last updated 8/24/2026
'''

import cv2
print("this program makes a meme with text ontop of a picture")

print('Make sure your picture is in the same folder as this script')

# Take keyboard input from user to retreive file name (Picture on their computor)

picture_file = (input('Enter the name of your picture file, including the extension, then press enter:'))


# Read the image file

picture = cv2.imread(picture_file)

# Resize picture to standard dimentions

resized_picture = cv2.resize(picture, (700, 350), interpolation=cv2.INTER_LINEAR)


# Take keyboard input from user to retreive text user wants to add ontop of image.
# This is stored as a new variable (picture_text)

picture_text = (input('Enter the text you want added to your image. Please stay under 23 characters:'))

# Add text ontop of cat.jpg
                                                # Coordinates
cv2.putText(resized_picture, picture_text, (10,100),
    cv2.FONT_HERSHEY_SIMPLEX, .75, (255,255,0) , 4)
                     # FONT SIZE,   COLOR,    THICKNESS
#Show the picture with the added text

cv2.imshow('Meme' , resized_picture)
#Record the waitkey preessed by user and create a new variable
keypressed = cv2.waitKey(0)


while keypressed != 27:
    print('invalid key:',keypressed)
    keypressed = cv2.waitKey(0)

#Now only way to do this is if user presses esc
cv2.destroyAllWindows()

cv2.imwrite('Newpic.jpg', resized_picture)