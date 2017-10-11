"""
Program using bitwise to check if a number is odd or even.

Works on the basis of if even it will have a 0 in the rightmost bit, if odd it will have a 1 in the rightmost bit
hence the return of number & 1 will return True if odd and false is even....
"""


def is_even(number):
	return not number & 1



if __name__ == "__main__":
	assert is_even(200) == True
	assert is_even(321) == False
