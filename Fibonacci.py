def fib(num):
    a=0
    b=1
    c=a+b
    print(a,"\t",end="")
    print(b,"\t",end="")
    print(a+b,"\t",end="")
    for i in range (2,num):
        a=b
        b=c
        c=a+b
        print(c,"\t",end="")
#num=int(input("\n enter number \n"))
#fib(num)
fib(10)
