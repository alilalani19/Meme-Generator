#This script is meant to showcase my understanding of basic python skills needed to complete the EYW Meme Maker Project.
#Written by Ali Lalani
#Last updated 9/9/2026

'''
PYTHON SKILLS

In python, proper syntax is essential or else your python script will not run as per syntax errors. Below is some syntax needed for python.

An indentation is a white space in a text. Indentation can be seen in languages for the purpose of readability.
Python uses indentation to create blocks of code. One indent is equal to 4 spaces or one tab. After a colon is present,
indentation is needed on the next line. Syntax is what allows a computor to understand python code. For example:
'''
x = int(input ('pick a number'))
if x > 15:
    print('Good Job!')
else:
    print('nice try!')
'''
In this portion, x is acting as a variable. A varible is used to store data for the script to refrence while
the script runs. The variable x is storing the integer the user enters.
'''


'''
Additionally, Python is case sensitive, for example all integrated python function should be lowecase.
While using libraries, ensure you have read the appropriate Docs for capitalization, etc. Comments should also be used
In order to explain what each significant line of code is doing.
Below is an example of both:
'''

#is_goated variable is set to true (bool), therefore when true: "SJS is Goated!" is printed
is_goated = True

if is_goated:
    print('SJS is Goated!')

#Data types
'''
Strings are text wrapped in quotes, this is used for messages, names, etc. What you want printed out For example:
'''
if is_goated:
    print('SJS is Goated!')
        # This right here is a string (inside parenthesis).


#complex numbers are represented by a real number, followed by an imaginary number with j attached.
y = 19 + 71j #complex

#Integers are positive and negative whole numbers. In python, integers are represented by int
z = 3 #int

#floats are real numbers with decimals, floats can also represent scientific notation.

f = 3.14159 #float

# Casting is converting one data type to another. For example, float to int.
x = int(input ('pick a number')) #Whatever numerical value the user enters will be converted into an integer via rounding.
if x > 15:
    print('Good Job!')
else:
    print('nice try!')

# A bool was used in code above that has been repasted for conveince. A bool sets a variable to True or Fale, similar to a light switch (On/Off)
is_goated = True #bool (is_goated set to True)

if is_goated:
    print('SJS is Goated!')
    
#Lists are a built in python data type, used to store multiple pieces of info in one variable
school = ['St. Johns', '2401 Claremont Ln', 'Day 2'] #list. If you print school, the output would be the contents inside list.

#Tuples are similar to lists, although they can not be changed after created.

t = ('white', 'black', 'green') #This is a tuple, similar to a list but can not be altered.
print(t[0]) #This prints the first piece of data in the tuple (order starts from 0 not 1)

#sets are similar to lists, although they are not ordered and do not allow for duplicates.
s = {'Ali', 'Major', 'Trey'} #set

#In Python, a dictionary is a built in data type used to store data in key and value pairs.

#this is a dictionary
dictionary = {
    'name':'Ali',
    'age':'15'
}
print(dictionary['name']) #output will be Ali

#If statements used for conditional decision making based on user input.
x = int(input ('pick a number')) #if the user chooses a number greater than 15, 1st print statement is triggered.
if x > 15:
    print('Good Job!')
else:
    print('try again') #if the users input is less than 15, 2nd print statement is triggered
    
#A match statement looks at a variable, finds the cases that matches its value, and only runs that values code.
    
status = 'Error'
match status: #match command matches the status to its case, and prints the appropriate response
    case 'Valid':
        print('Success!')
    case 'Error':
        print('contact Ali for support') #match response for 'Error'
#A while loop is used to repeat a block of code over and over as long as a specific condition stays True

cookies = 3 # a while loop is used here to track inventory of cookies. Inventory starts out at 3 and reduce by 1 cookie. When there is less than 1 cookie left, the print command is triggered.
while cookies >1:
    print('Cookies available!')
    cookies = cookies - 1
print('Out of treats!')

#A function is a reusable block of code that only runs when you it is called.
def greeting(): #every time greeting function is called, print command is triggered.
    Print('Hi Ms. Faulk!')

greeting() #This triggers the print command.