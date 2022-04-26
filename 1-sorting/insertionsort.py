
def insertionsort(A):
	for i in range(len(A)):
		temp = A[i]
		red = i-1
		while red >= 0 and A[red] > temp:
			A[red+1] = A[red]
			red = red-1
		A[red+1] = temp
	return A

print(insertionsort([9,2,8,1,7,4,5]))
