# Time: O(n**2)
# Space O(n)

# SELECTION SORT

def selectionsort(A):
	for i in range(len(A)):
		minvalue = A[i]
		minindex = i
		for red in range(i+1, len(A)):
			if A[red] < minvalue:
				minvalue = A[red]
				minindex = red
		A[i], A[minindex] = A[minindex], A[i]
	return A

print(selectionsort([4, 3, 6, 5, 8, 2]))
