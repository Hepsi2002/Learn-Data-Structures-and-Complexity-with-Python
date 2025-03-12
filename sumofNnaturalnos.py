'''def SumN(N):
    sum=0
    for i in range(1,N+1):
        sum=sum+i
    print(sum)
SumN(10)'''

def SumofN(n):
    if n==1:
        return 1
    return SumofN(n-1)+n

print(SumofN(10))