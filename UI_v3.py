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
        selected_file_path = file_path
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

#function 2 (allows user to add text ontop of an image via our UI
def process_meme():
    global selected_file_path
    
    if not selected_file_path:
        print('Please upload picture before adding text')
        return
    
    meme_text = text_entry.get()
    if len(meme_text) > 23:
        print('Please limit text to 23 characters')
        
    picture = cv2.imread(selected_file_path)
    
    cv2.putText(picture, meme_text, (10,100),
    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,0) , 4)
    
    output_name = 'Meme_Image.jpg'
    cv2.write(output_name, picture)
    print('Meme successfully saved. File name is: {output_name}!')
    
        

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

#Box for user to enter text for meme
entry_label = ctk.CTkLabel(root, text="2. Enter Meme Text (Under 23 Characters):")
entry_label.pack(pady=5)

text_entry = ctk.CTkEntry(root, width=350, placeholder_text="Type meme text here...")
text_entry.pack(pady=10)

btn_make = ctk.CTkButton(root, text='3. Generate and Save Meme (Ali always has your back)', fg_color="green", hover_color="darkgreen", command=process_meme)
btn_make.pack(pady=20)

root.mainloop()