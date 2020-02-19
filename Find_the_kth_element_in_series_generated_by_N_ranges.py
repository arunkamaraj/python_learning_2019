# Python3 implementation of the approach

# Function to return the kth element
# of the required series
def getKthElement(n, k, L, R):
	l = 1
	h = n

	# To store the number of integers that lie
	# upto the ith index
	total=[0 for i in range(n + 1)]

	total[0] = 0

	# Compute the number of integers
	for i in range(n):
		total[i + 1] = total[i] + (R[i] - L[i]) + 1

	# Stores the index, lying from 1
	# to n,
	index = -1

	# Using binary search, find the index
	# in which the kth element will lie
	while (l <= h):
		m = (l + h) // 2

		if (total[m] > k):
			index = m
			h = m - 1
		elif (total[m] < k):
			l = m + 1
		else :
			index = m
			break

	l = L[index - 1]
	h = R[index - 1]

	# Find the position of the kth element
	# in the interval in which it lies
	x = k - total[index - 1]

	while (l <= h):
		m = (l + h) // 2

		if ((m - L[index - 1]) + 1 == x):
			return m

		elif ((m - L[index - 1]) + 1 > x):
			h = m - 1

		else:
			l = m + 1

# Driver code

L=[ 1, 8, 21]
R=[4, 10, 23]
n = len(L)

k = 6

print(getKthElement(n, k, L, R))

p =[1,2,3,4,8,9,10,21,22,23]