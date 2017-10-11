def minmax(data):
	min = float("inf")
	max = float("-inf")

	for i in data:
		if i > max:
			max = i
		if i < min:
		 	min = i

	return (min, max)


if __name__ == "__main__":
	assert minmax([1, 2, 3, 4, 5]) == (1, 5)

