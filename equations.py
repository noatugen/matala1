
def power(x,a):
    b=1.0
    if a>=0 :
        i=a
        while i>0:
            b=b*x
            i=i-1
        return float(b)
    elif a<=0:
         i=a*(-1)
         while i>0:
            b=b*x
            i=i-1
         return float(1/b)

def assembly(x):
    if x<0:
        return 0.0
    elif x==0:
        return float(1)
    for i in range(2,int(x)+1):
        x=x*(i-1)    
    return float(x)

def exponent(x):
    n=100
    e=1
    for i in range(1,n+1):
        e=e+power(x, i)/assembly(i)
    return e

def ln(x):
    try:
        if x<= 0:
            return 0.0
        y_n = x-1.0
        while True:
            ex = exponent(y_n)
            y_n1 = y_n+2*((x-ex)/(x+ex))
            if (y_n-y_n1) <= 0.001 and (y_n1-y_n) <= 0.001:
                return float(y_n1)
            y_n=y_n1
    except:
            return(0.0)
        
def XtimesY(x:float,y:float) -> float:
    try:
        if (x<=0):
            return 0.0
        else:
            ans = exponent(ln(x)*y)
            return float('%0.6f' % ans)
    except:
        return(0.0)
    
def sqrt(x:float,y:float) -> float:
    try:
        if (y>0 and x!=0):
            x=1/x
            a=(XtimesY(y,x))
            return float('%0.6f' %a)
        else:
            return(0.0)
    except:
        return (0.0)

def calculate(x):
    try:
        if x<=0 :
            return 0.0
        ans= exponent(x)*power(7,x)*power(x,-1)*sqrt(x,x)
        ans1= float('%0.6f' %ans)
        return ans1
    except:
        return (0.0)
print(calculate(0))
   
# try:
    num=input("Enter a num: ")
    num= float(num)
    ans=calculate(num)
    return float('%0.6f' %ans)
# except:
#     return 0.0
    
























            
            
            
            
         
            