#author jiseonmin 
##Euler method
#1
import numpy as np

def spring(x0,v0,h,n):
    x = np.zeros(n)
    v = np.zeros(n)
    t = np.zeros(n)
    x[0] = x0
    v[0] = v0
    for i in range(n-1):
        x[i+1] = x[i]+h*v[i]
        v[i+1] = v[i]-h*x[i]
        t[i+1] = h*(i+1)
    return x,v,t

import matplotlib.pyplot as plt
f = spring(0,10,0.0001,300000)

plt.figure()
plt.plot(f[2],f[0])
plt.xlabel('time')
plt.ylabel('position')
plt.figure()
plt.plot(f[2],f[1])
plt.xlabel('time')
plt.ylabel('velocity')
plt.savefig('w3fig2.png')
plt.clf()

#2
xexc = 10*np.sin(f[2])
vexc = 10*np.cos(f[2])
plt.figure()
plt.plot(f[2],(xexc-f[0]))
plt.xlabel('time')
plt.ylabel('global error of position')
plt.figure()
plt.plot(f[2],(vexc-f[1]))
plt.xlabel('time')
plt.ylabel('global error of velocity')
plt.savefig('w3fig3.png')
plt.clf()
# #3
# h0=0.0003
# hlist = [h0,h0/2,h0/4,h0/8,h0/16]
# xerror = np.zeros(5)
# for i in range(5):
#     f=spring(0,10,hlist[i],300000*2**i)
#     xexc = 10*np.sin(f[2])
#     xerror[i] = np.max((xexc-f[0]))
# plt.figure()
# plt.loglog(hlist,xerror,'.')
# plt.xlabel('h')
# plt.ylabel('truncation error')
# plt.show()
#
# #4
# f = spring(0,10,0.0003,300000)
# E = np.zeros(np.size(f[2]))
# for i in range(np.size(E)):
#     E[i] = f[0][i]**2 + f[1][i]**2
# plt.figure()
# plt.plot(f[2],E)
# plt.xlabel('time')
# plt.ylabel('energy')
# plt.show()
#
# #5 implicit euler
# def springimp(x0,v0,h,n):
#     x = np.zeros(n)
#     v = np.zeros(n)
#     t = np.zeros(n)
#     x[0] = x0
#     v[0] = v0
#     for i in range(n-1):
#         x[i+1] = x[i]/(1+h**2)+h*v[i]/(1+h**2)
#         v[i+1] = v[i]/(1+h**2)-h*x[i]/(1+h**2)
#         t[i+1] = h*(i+1)
#     return x,v,t
#
# h0=0.0003
# hlist = [h0,h0/2,h0/4,h0/8,h0/16]
# xerrorimp = np.zeros(5)
# xerror = np.zeros(5)
# for i in range(5):
#     f=springimp(0,10,hlist[i],300000*2**i)
#     g=spring(0,10,hlist[i],300000*2**i)
#     xexc = 10*np.sin(f[2])
#     xerrorimp[i] = np.max((xexc-f[0]))
#     xerror[i] = np.max((xexc - g[0]))
# plt.figure()
# plt.loglog(hlist,xerrorimp,'r.')
# plt.loglog(hlist,xerror,'g.')
# plt.xlabel('h')
# plt.ylabel('truncation error')
# plt.title('Comparing truncation error of Euler implicit & explicit')
# plt.show()
#
# f=springimp(0,10,0.0003,300000)
# g=spring(0,10,0.0003,300000)
# Eimp = np.zeros(np.size(f[2]))
# E = np.zeros(np.size(f[2]))
# for i in range(np.size(E)):
#     Eimp[i] = f[0][i]**2 + f[1][i]**2
#     E[i] = g[0][i]**2 + g[1][i]**2
# plt.figure()
# plt.plot(f[2],Eimp,'r')
# plt.plot(f[2],E,'g')
# plt.xlabel('time')
# plt.ylabel('energy')
# plt.show()
#
# # Part 2 - phase space
# f=springimp(0,10,0.003,30000)
# g=spring(0,10,0.003,30000)
# plt.figure()
# plt.plot(f[0],f[1],'r')
# plt.plot(g[0],g[1],'g')
# plt.xlabel('x')
# plt.ylabel('v')
# plt.show()
#
#
# # Symplectic
# def springsym(x0,v0,h,n):
#     x = np.zeros(n)
#     v = np.zeros(n)
#     t = np.zeros(n)
#     x[0] = x0
#     v[0] = v0
#     for i in range(n-1):
#         x[i+1] = x[i]+h*v[i]
#         v[i+1] = v[i]-h*x[i+1]
#         t[i+1] = h*(i+1)
#     return x,v,t
# i = springsym(0,10,0.003,30000)
# plt.figure()
# plt.plot(f[0],f[1],'r')
# plt.plot(g[0],g[1],'g')
# plt.plot(i[0],i[1],'b')
# plt.xlabel('x')
# plt.ylabel('v')
# plt.show()
#
# i = springsym(0,10,0.003,30000)
# Esym = np.zeros(np.size(i[2]))
# for j in range(np.size(Esym)):
#     Esym[j] = i[0][j]**2 + i[1][j]**2
# plt.figure()
# plt.plot(i[2],Esym,'b')
# plt.xlabel('time')
# plt.ylabel('energy')
# plt.show()
#
# # Lag of the symplectic solution over time
# i = springsym(0,10,0.03,300000)
# exc = 10*np.sin(i[2])
# plt.figure()
# plt.plot(i[2][299500:-1],i[0][299500:-1],'r')
# plt.plot(i[2][299500:-1],exc[299500:-1],'g')
# plt.xlabel('time')
# plt.ylabel('position')
# plt.show()
#
#
# #For bigger h, repeat the energy plot.
# f=springimp(0,10,0.003,300000)
# g=spring(0,10,0.003,300000)
# Eimp = np.zeros(np.size(f[2]))
# E = np.zeros(np.size(f[2]))
# for i in range(np.size(E)):
#     Eimp[i] = f[0][i]**2 + f[1][i]**2
#     E[i] = g[0][i]**2 + g[1][i]**2
# plt.figure()
# plt.loglog(f[2],Eimp,'r')
# plt.loglog(f[2],E,'g')
# plt.xlabel('time')
# plt.ylabel('energy')
# plt.show()
#
# #Also for phase space of symplectic method
# i = springsym(0,10,0.1,30000)
# plt.figure()
# plt.plot(i[0],i[1],'r')
# plt.plot(10*np.sin(i[2]),10*np.cos(i[2]),'b')
# plt.show()
