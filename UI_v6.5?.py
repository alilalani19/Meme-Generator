import cv2
import customtkinter as ctk
from customtkinter import filedialog
from PIL import Image

#set variables global throughout code
selected_file_path = None
#Set default color to light blue (BGR format)
chosen_color = (255, 255, 0) 

#Set the UI appearnce to user system default
ctk.set_appearance_mode('System')

#Set User UI button color and theme to Blue
ctk.set_default_color_theme('blue')

#Create a pull_file comand which opens finder to select image
def pull_file():
    global selected_file_path
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

#New function to allow user to select a color based on their prefrence (4 colors via 4 checkboxes)
def select_color(color_name):
    global chosen_color
    
    #deselects all checkboxes as default so user can select
    check_cyan.deselect()
    check_red.deselect()
    check_green.deselect()
    check_blue.deselect()
    
    #select the clicked box one and map it to OpenCV BGR color format
    if color_name == "Cyan":
        check_cyan.select()
        chosen_color = (255, 255, 0)
                    #BGR format for light blue
    elif color_name == "Red":
        check_red.select()
        chosen_color = (0, 0, 255)
                    #BGR for red
    elif color_name == "Green":
        check_green.select()
        chosen_color = (0, 255, 0)
                    #BGR for green
    elif color_name == "Blue":
        check_blue.select()
        chosen_color = (255, 0, 0)
                    #BGR for Blue (diffrent than light blue)
        
        
#function 3 (allows user to add text ontop of an image via our UI)
def process_meme():
    
    #If user does not input a file (their picture), text is printed to signal user.
    if not selected_file_path:
        print('Please upload picture before adding text')
        return
    # First store the inputed meme text into a new variable, then if the meme text is over 23 characters,
    # user is asked to limit text.
    meme_text = text_entry.get()
    if len(meme_text) > 23:
        print('Please limit text to 23 characters')
    # store file (picture) as a new variable and process that image with cv2 lib    
    picture = cv2.imread(selected_file_path)
    # Add text ontop of image, located at (10,100)
    cv2.putText(picture, meme_text, (25,125),
    cv2.FONT_HERSHEY_SIMPLEX, .75, chosen_color , 4)
    
    #store the name and format of new pic as a new variable and save the new meme via cv2 lib
    output_name = 'Meme_Image.jpg'
    cv2.imwrite(output_name, picture)
    print(f'Meme successfully saved. File name is: {output_name}!')
    
        
# Create a UI window which is launched for the User
root = ctk.CTk()
# Create title for UI window
root.title('Meme Generator')
#Def dimentions for UI window
root.geometry('1000x700')

#Create a button in user UI that runs pull_file func when pressed
btn_pull = ctk.CTkButton(root, text='Upload Image', command = pull_file)
btn_pull.pack(pady=50)

#Create a blank area for image placeholder before image is uploaded
img_label = ctk.CTkLabel(root, text='No image uploaded.', width=400, height= 300, fg_color="gray25" if ctk.get_appearance_mode() == "Dark" else "gray75")
img_label.pack(pady=20)

#Text in box for user to enter text for meme
entry_label = ctk.CTkLabel(root, text="2. Enter Meme Text (Under 23 Characters):")
entry_label.pack(pady=5)

#Text to prompt user to select color of text
color_label = ctk.CTkLabel(root, text="3. Select Text Color:")
color_label.pack(pady=5)

#create a frame where the checkboxes will be side by side
checkbox_frame = ctk.CTkFrame(root, fg_color="transparent")
checkbox_frame.pack(pady=5)

#Create a checkbox for Cyan
check_cyan = ctk.CTkCheckBox(checkbox_frame, text="Cyan (Default)", command=lambda: select_color("Cyan"))
check_cyan.pack(side="left", padx=10)
check_cyan.select() #light blue/cyan is selected as default, user can change

#Create a checkbox for Red
check_red = ctk.CTkCheckBox(checkbox_frame, text="Red", command=lambda: select_color("Red"))
check_red.pack(side="left", padx=10)

#Create a checkbox for Green
check_green = ctk.CTkCheckBox(checkbox_frame, text="Green", command=lambda: select_color("Green"))
check_green.pack(side="left", padx=10)

#Create a checkbox for Blue
check_blue = ctk.CTkCheckBox(checkbox_frame, text="Blue", command=lambda: select_color("Blue"))
check_blue.pack(side="left", padx=10)


#Text inside entry box to signal user where to enter text.
text_entry = ctk.CTkEntry(root, width=350, placeholder_text="Type meme text here...")
text_entry.pack(pady=10)

#Attach Button to process meme function. Allows user to generate/process and save meme with click of a putton
btn_make = ctk.CTkButton(root, text='3. Generate and Save Meme (Ali always has your back)', fg_color="green", hover_color="darkgreen", command=process_meme)
btn_make.pack(pady=20)

root.mainloop()