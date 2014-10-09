import sys
import pdb
from random import choice

random1 = [1,2,3,4,5,6,7,8,9,10,11,12]
random2 = [1,2,3,4,5,6,7,8,9,10,11,12]

while True:
	num1 = choice(random1)
	num2 = choice(random2)
	print "To Exit this game type 'exit'"
	answer = raw_input("What is {} times {} ?".format(num2, num1))
	

	# exit
	if answer == "exit":
		print "Now exiting game!"
		sys.exit()
	elif int(answer) == num2 * num1:
		print "Correct!"
		break
	else:
		print "Wrong!"