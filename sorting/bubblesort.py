# Time: O9N**2)
# Space: O(n)

# Bubble Sort

def bubblesort(A):
	for i in range(len(A)):
		for red in range(len(A)-1, i, -1):
			if A[red-1] > A[red]:
				A[red-1], A[red] = A[red], A[red-1]
	return A

print(bubblesort([6,5,4,8,7,2,1,9,3]))
