a="aryan"
b=len(a)
for i in range(b):
 print(i,a[i])

z=3
for i in range(1,11):
    print(z,"*",i,"=",i*z)
 
print("\n")

for i in range(10,0,-1):
  print(z,"*",i,"=",i*z)

c=[1,2,3,4,5]
s=0
l=1
for i in range(1,6):
  s=s+i
  l=l*i
print(s,l)

e=[]
o=[]
for i in c:
  if(i%2==0):
    e.append(i)
  else:
    o.append(i)

print("even=",e,"odd=",o)


a=int(input("Enter Num: "))
for i in range(1,11):
    print(a,"*",i,"=",a*i)