num=int(input("Enter the Number :"))
for i in range(num+1):
	for j in range (1,1+i):
		print(j,end=" ")
	print("\n")

for i in range(num):
	for j in range (1,num+1-i):
		print(j,end=" ")
	print("\n")

for j in range(x):
    print("-"*(x-j),('$'*(j+1)))
    # print("\n")