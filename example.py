def sum (n):
    if(n>0):
        sum(n-1)
    print n
sum(1)