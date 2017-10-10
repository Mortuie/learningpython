"""
try and catch statements essentially in python.

Use sparsely, they are quite slow and more often used
when you know errorneous inputs will be rare, but might 
occur.

"""


def main():

	age = -1

	while age <= 0:
		try:
			age = int(input("What is your age?"))
			if age <= 0:
				print("Your age must be positive")
		except ValueError:
			print("That is an invalid age...")
		except EOFError:
			print("There was an unexpected input whilst reading the input")
		except SyntaxError:
			print("Invalid input syntax...")
		except NameError:
			print("Invlaid input")
		



if __name__ == "__main__":
	main()
