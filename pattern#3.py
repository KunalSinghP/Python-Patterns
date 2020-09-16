n = int(input("Enter No. of Rows: \n"))
x=1
for i in range(1,n+1):
   print(x,end=" ")
   x+=1
   for j in range(n-1,0,-1):
      print(j,end=" ")
   print()
