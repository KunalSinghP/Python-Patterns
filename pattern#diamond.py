n=int(input("No. of rows \t:"))
f=1
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))
for j in range(n-1,0,-1):
    print(" "*(f)+"* "*(n-f))
    f+=1
    
    
  
