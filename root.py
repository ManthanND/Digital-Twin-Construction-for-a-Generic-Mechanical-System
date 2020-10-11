import numpy as np

from sympy import symbols, diff
from sympy import *
from numpy.linalg import inv
import math


            
def newton_root_multi(function_1,guess_vector):
    x1=symbols('x1',real=True)
    x2=symbols('x2',real=True)
    x3=symbols('x3',real=True)
    y1=function_1[0]
    f1=function_1[0]
    ###y1=(3*x1)-float(math.cos(x2*x3))-(3/2)
    ###f1=(3*x1)-float(math.cos(x2*x3))-(3/2)
    d11=diff(f1,x1)
    d12=diff(f1,x2)
    d13=diff(f1,x3)
    y2=function_1[1]
    f2=function_1[1]
    ###y2=(4*x1*x1)-625*(x2*x2)+(2*x3)-1
    ###f2=(4*x1*x1)-625*(x2*x2)+(2*x3)-1
    d21=diff(f2,x1)
    d22=diff(f2,x2)
    d23=diff(f2,x3)
    y3=function_1[2]
    f3=function_1[2]
    ###y3=(20*x3)-float(math.exp((-x1)*x2))+9
    ###f3=(20*x3)-float(math.exp((-x1)*x2))+9
    d31=diff(f3,x1)
    d32=diff(f3,x2)
    d33=diff(f3,x3)

    n=1
    i=0
    while 1:

        J=[[d11,d12,d13],[d21,d22,d23],[d31,d32,d33]]
        if i==0:
            x1=float(guess_vector[0])
            x2=float(guess_vector[1])
            x3=float(guess_vector[2])
            G=np.array([x1,x2,x3]).T
        else:
            G=s
            x1=G[0]
            x2=G[1]
            x3=G[2]
        e11=eval(str(d11))
        e12=eval(str(d12))
        e13=eval(str(d13))
        e21=eval(str(d21))
        e22=eval(str(d22))
        e23=eval(str(d23))
        e31=eval(str(d31))
        e32=eval(str(d32))
        e33=eval(str(d33))
        J=[[e11,e12,e13],[e21,e22,e23],[e31,e32,e33]]
        J=np.array(J)
        print(J)
        JI=inv(J)

        f1=eval(str(y1))
        f2=eval(str(y2))
        f3=eval(str(y3))
        F=[f1,f2,f3]
        F=np.array(F).T
        print(F)
        c=np.matmul(JI,F)
        print(c)
        s=np.subtract(G,c)
        n=n+1
        print(n)
        print(s)
        i=i+1
        if G[0]==s[0]:
            break
    print("Answer is:")
    print(s)
    return(s)     
    
x1=symbols('x1',real=True)
x2=symbols('x2',real=True)
x3=symbols('x3',real=True)
f=[x1+x2+x3-2,
   (6*x1)-(4*x2)+(5*x3)-315,
   (x1)+(2*x2)+(2*x3)-13]
g=[2,2,3]
y=newton_root_multi(f,g)


