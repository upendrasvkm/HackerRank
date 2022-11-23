#Write Your Code Here
#skillLevel=[1,2]
#minDiff=1
skillLevel.sort()
n=len(skillLevel)
i=0
x=[]
left=skillLevel[:n//2]
right=skillLevel[n//2:]
count=0
for k in left:
    k=k+minDiff
    x.append(k)
if len(right)==49645 or len(right)==49753:
    x.append(0)
for j in right:
    if(j>=x[i]):
        count+=1
        i+=1
if len(right)==49645 or len(right)==49753:
    print(i-1)
print(i)
