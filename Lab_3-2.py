
#Create a Python file named lab_3-2.py
#Copy the following examples into a Python file one at a time. 
#Think about what kind of error you think it will throw before running the code. 
#When you have run one line, be sure to comment it before adding your next line.
#After you have commented out a line, add a comment listing what error type occured.
	
#int(a)
 #NameError name 'a' not defined
 #Correct
#int('a')
 #ValueError:invalid literal for int() with base 10: 'a'
 #Correct
#'a' + 2
 #TypeError must be str not int
 #Wrong TypeError: can only concatenate str (not "int") to str
#import date
 #ModuleNotFoundError: no module named 'date' 
 #Correct
#print("I'm a happy camper!)
 #syntaxError expected " did you mean print("I'm a happy camper!")
 #Wrong SyntaxError: unterminated string literal (detected at line 20)

