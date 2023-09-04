def permutation(x,y,z,n):
	hasil = []
	for x in range(0, n+1):
		for y in range(0, n+1):
			for z in range(0, n+1):
				if x <= y <= z and x+y+z <=n:
					hasil.append((x,y,z))
	return hasil
	
def main():
	x = int(input())
	y = int(input())
	z = int(input())
	n = int(input())

	permutations = permutation(x,y,z,n)

	for permutation in permutations:
		print(permutation)


main()