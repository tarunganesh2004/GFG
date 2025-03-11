# Ways to reach the nth Stair

n=1

# recursion
def recursion(n):
    def f(n):
        if n==0:
            return 1
        if n<0:
            return 0
        return f(n-1)+f(n-2)+f(n-3)
    return f(n)

print(recursion(n)) # 1