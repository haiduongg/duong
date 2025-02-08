A=[]
d=0

n=int(input("nhập số nguyên n: "))
for i in range (n):
	dw=int(input("nhập số thứ " + str(i+1)+":"))
	A.append(dw)

print("dãy số đã nhập:")

for i in range(n):
	print(A[i], end =" ")
	if A[i]%2==1:
		d=d+A[i]

print("tổng số lẻ:"+str(d))
