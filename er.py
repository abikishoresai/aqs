t=int(input())
s=""
for i in range(1,t+1):
    if t%i==0 and i%2==1:
        s=s+str(i)+" "
print(s.strip())
