def armstrong(num):
    n=num
    sum=0
    while (num > 0):
        r=num%10
        sum=sum+r*r*r
        num=num/10
        print(sum)
        
    if (n==sum):
        print(sum)
        print('Armstrong number')
    else:
        print(sum)
        print('Not Armstrong number')
        

num = int(input("Enter a number: "))
armstrong(num)
