def SieveOfEratosthenes(n):
    prime=[True for i in range(n+1)]
    p=2
    totSum=0
    while(p*p<= n):
        if(prime[p]==True):
            for i in range(p*p, n+1, p):
                prime[i]=False
        p+=1
    for p in range(2, n+1):
        if prime[p]:
            totSum+=p
    print(totSum)

n=2*10**6
print(f"Following is the sum of prime below {n}\n")
SieveOfEratosthenes(n)
