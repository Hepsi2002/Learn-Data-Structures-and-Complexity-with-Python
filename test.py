#Iterative
'''def cal(n):
    while n>0:
        k=n**2
        print(k)
        n=n-1

n=int(input("enter a num"))
cal(n)

#Recursive
def cal(n):
    if n>0:
        k=n**2
        print(k)
        cal(n-1)

n=int(input("enter a num"))
cal(n)'''
def cal(n):
    if n>0:
        cal(n - 1)
        k=n**2
        print(k)
        cal(n-1)


cal(4)