s=int(input())
if s>=-2**15+1 and s<=2**15+1:
    print("INT")
elif s>=-2**31+1 and s<=2**31+1:
    print("LONG")
else:
    print("LONG LONG")
