#1.1 Implement a recursion function to calculate factorial of a given number


def fact_rec(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)


n=2
res=fact_rec(n)

print("the factorial of {} is {}".format(n,res))