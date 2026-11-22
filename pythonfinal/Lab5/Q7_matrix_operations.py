# Square matrices
n = int(input("Matrix size (n): "))
print("Enter matrix A row-wise:")
a = [list(map(float, input().split())) for _ in range(n)]
print("Enter matrix B row-wise:")
b = [list(map(float, input().split())) for _ in range(n)]
add = [[a[i][j]+b[i][j] for j in range(n)] for i in range(n)]
sub = [[a[i][j]-b[i][j] for j in range(n)] for i in range(n)]
mul = [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
div = [[a[i][j]/b[i][j] if b[i][j] != 0 else "undefined" for j in range(n)] for i in range(n)]
transpose = [[a[j][i] for j in range(n)] for i in range(n)]
trace = sum(a[i][i] for i in range(n))
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Element-wise division:", div)
print("Transpose A:", transpose)
print("Trace A:", trace)
