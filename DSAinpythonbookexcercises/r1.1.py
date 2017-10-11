def is_multiple(n, m):
	return n % m == 0


if __name__ == "__main__":
	print(is_multiple(20, 10))
	assert is_multiple(20, 10) == True
	assert is_multiple(10, 20) == False
