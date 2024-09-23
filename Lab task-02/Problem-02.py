a=[1,3,5,7,4]
print(sum(num for num in a if num % 2 != 0))

sum=0
for i in range(len(a)):
    if i%2==1:
        sum=sum+a[i]
print(sum)

odd=0
even=0
for i in a:
    if i%2==0:
        even+=1
else:
    odd+=1
print("Even: ",even,",","Odd:",odd)