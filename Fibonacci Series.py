def fibonacci(n):
    if n==0:
        return 1
    if n==1:
        return 1
    
    last =fibonacci(n-1)
    secondlast = fibonacci(n-2)

    ans = last + secondlast

    return ans

print(fibonacci(5))

