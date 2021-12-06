n=int(raw_input("Enter the limit :"))
a=0
b=1
if n>0:
    if n==1:
        print a
    else:
        print a
        print b
        i=3
        while i<=n:
            c=a+b
            print c
            a=b
            b=c
            i=i+1

else:
    print "ERROR"
