import numpy as np
from numpy.linalg import inv

import matplotlib.pyplot as plt
plt.close('all')
# f = lambda x : 11*np.power(np.cos(0.5*x),2)  + np.power(x,4)/100 + 7*np.sin(2*x)
f = lambda x : np.power(1 + np.power(x,2) , -1)
x = np.arange(-10,10.5,0.5)
y = f(x)
hh = 0.01


# x[3] = 12
idx = np.argsort(x)
y = y[idx]

n = np.max(len(x)) -1
A = np.zeros((n+3,n+3))
A[0:n+1,0] = np.reshape(np.ones((n+1,1)),(len(x),))
A[0:n+1,1] = x
A[n+1,2:n+4] = np.ones((1,n+1))    
A[n+2,2:n+4] = np.reshape(x,(1,len(x)))  
for k in range(0,n):
    # print(i)
    for j in range(0,k+1):
        # print(k,j)
        A[k+1,j+2] = np.power((x[k+1] - x[j]),3)
Y = np.zeros((n+3,1))
Y[0:n+1,0] = np.reshape(y,(len(x),)) 

xx = np.arange(-10,10.01,0.01)
N = len(xx)


cof = np.dot(inv(A),Y)

S = np.dot(cof,np.ones((1,N)))
S[1,:] = np.multiply(S[1,:],xx)
for i in range(2,n+3,1):
    x_x = np.power((xx - x[i-2]),3)
    idx = x_x < 0
    x_x[idx] = 0
    S[i,:] = np.multiply(S[i,:],x_x)
yy = np.sum(S,axis = 0)
xxx = np.arange(-10,10.1,0.1)
plt.figure()
plt.plot(x,y,'o')
plt.plot(xx, yy,color = 'r')
plt.plot(xxx, f(xxx),'.g')
plt.grid()
plt.legend(['Data of Function h = 1','Cubic Spline h = 0.01','Function h = 0.1'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Cubic Spline and F(x)')

plt.figure()
plt.plot(x,y,label='f(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('Function $f = 11 cos(0.5x) ^2 + 7 sin(2x) + x^4$')

# np.sqrt(np.sum(np.power(f(xxx)-yy,2)))