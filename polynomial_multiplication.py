def DFT(A, b, d, n):

	product = [0] * (d + n - 1);
	

	for i in range(d):
		
		for j in range(n):
			product[i + j] += A[i] * b[j];

	return product;

def print_poly(poly, n):

	for i in range(n):
		print(poly[i], end = "");
		if (i != 0):
			print("x^", i, end = "");
		if (i != n - 1):
			print(" + ", end = "");


# This array represents a polynomial function : 4 + 0x^ 1 + 10x^ 2 + 5x^ 3
A = [4, 0, 10, 5];

# This array represents a polynomial function : 1 + 2x^ 1 + 5x^ 2
b = [1, 2, 5];

d = len(A);
n = len(b);

print("The first polynomial is ",);
print_poly(A, d);
print("\nThe second polynomial is ");
print_poly(b, n);

product = DFT(A, b, d, n);

print("\nProduct of two polynomials is ");
print_poly(product, d+n-1);