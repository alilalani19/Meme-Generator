import cv2
import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image

#Set the UI appearnce to user system default
ctk.set_appearance_mode('System')

#Set User UI button color and theme to Blue
ctk.set_default_color_theme('blue')

#Create a pull_file comand which opens finder to select image
def pull_file():
    file_path = filedialog.askopenfilename(title="Select an Image")
    if file_path:
        print(f"File selected: {file_path}")
        
        #Load image via PIL library (included w/ customtkinter lib)
        pil_image = Image.open(file_path)
        
        #Convert pil image (python imaging library) to ctk image for UI
        ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(400, 300))
        
        #Change label while program is running for placeholder text
        img_label.configure(image=ctk_image, text="")
        
        #Python deletes file data after function is done running, therefore we need to keep file data by attaching it to the "label" itself
        img_label.image = ctk_image
        
    else:
        print('No file selected')

# Create a UI window which is launched for the User
root = ctk.CTk()
# Create title for UI window
root.title('Meme Generator')
#Def dimentions for UI window
root.geometry('1000x500')

#Create a button in user UI that runs pull_file func when pressed
btn_pull = ctk.CTkButton(root, text='Upload Image', command = pull_file)
btn_pull.pack(pady=50)

#Create a blank area for image placeholder before image is uploaded
img_label = ctk.CTkLabel(root, text='No image uploaded.', width=400, height= 300, fg_color="gray25" if ctk.get_appearance_mode() == "Dark" else "gray75")

img_label.pack(pady=20)

root.mainloop()