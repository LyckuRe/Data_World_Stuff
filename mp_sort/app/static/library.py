from org.transcrypt.stubs.browser import *
import random

array = []

def gen_random_int(number, seed):
	random.seed(seed)
	integer = random.randint(1,number)
	return integer

def generate():
	global array
	
	number = 10
	seed = 200
	# empty the array before every generation
	array = []
	# call gen_random_int() with the given number and seed
	# store it to the global variable array
	for i in range(10):
		array.append(gen_random_int(number, seed))
	pass

	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	array_str = str(array)[1:-1] + '.'
	pass

	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the global variable array and 
			copy it to a new list
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	global array

	n = len(array)
	for i in range(1,n):
		for j in range(1,n):
			if array[j] < array[j-1]:
				array[j], array[j-1] = array[j-1], array[j]

	pass

	array_str = str(array)[1:-1] + '.'
	
	document.getElementById("sorted").innerHTML = array_str


def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementById("value").value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return

	# Your code should start from here
	# store the final string to the variable array_str
	else:
		array = value.split(',')
		n = len(array)
		for i in range(1,n):
			for j in range(1,n):
				if int(array[j]) < int(array[j-1]):
					array[j], array[j-1] = array[j-1], array[j]

	pass

	#array_str = str(array)[1:-1] + '.'
	array_str = array
	document.getElementById("sorted").innerHTML = array_str