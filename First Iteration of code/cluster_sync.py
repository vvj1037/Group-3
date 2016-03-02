import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from random import randint
import random

# First set up the figure, the axis, and the plot element we want to animate
print "Please Place the appropriate adjacency matrix file in the same folder as this file and name it net_adj.dat"
print "Enter The No. of Nodes"
SIZE=int(raw_input())

print "Enter The Value of e"
e=float(raw_input())

print "Enter The Value of Mu"
MU=float(raw_input())

#MU=MU/float(10)


adjacent=[]
for i in range(0,1001):
        adjacent.append([])
with open('net_adj.dat') as f:
    for line in f: # read rest of lines
        x,y=map(int,line.split())
        adjacent[x].append(y)



# MU=2
# e=0.8
# SIZE=1000
TIME=100
parent=[]
occur=[]
a=[]
prev=[]
times_occur=[]
ts=["" for _ in range(0,1001)]
maxima=[]
class particles(object):

    #INITIALIZATION OF ARRAYS
    for i in range(1001):
        a.append([])
        prev.append([])
        for j in range(101):
            a[i].append(randint(1,9)/float(10))
    #a[1][0]=0.2

    
    for i in range(0,101):
        occur.append([])
        for j in range(0,1001):
            occur[i].append(0)
    
    vis=[]
    counter=0
    for i in range(1001):
        maxima.append([])
        #ts.append([])
        parent.append(0)
        vis.append(0)
    

    for _ in range(0,TIME+1):
        times_occur.append([])
        

    # for i in range(TIME+1):
    #     times_occur.append(0)

    #INITIALIZATION COMPLETE

    #COMPUTING FUNCTIONS DEFINED
    
    def initi(self):
        global SIZE,parent
        for i in range(SIZE-1):
            parent[(i+1)]=i+1
    def func(self,x):
        global MU
        return MU*abs(x)*(1-abs(x))

    def fill(self):
        global SIZE,a,adjacent,func,TIME
        for j in range(0,TIME):
            for i in range(1,SIZE+1):
                val=self.func(a[i][j])
                a[i][j+1]=(1-e)*val
                add=0
                ctr=0
                for k in range(0,len(adjacent[i])):
                    adjnode=adjacent[i][k]
                    ctr=ctr+1
                    add=add+(self.func(a[adjnode][j])-val)
                add=(e*add)/float(ctr)
                #print add
                a[i][j+1]=a[i][j+1]+add
                

    def analyze(self):
        global SIZE,a,occur,maxima,times_occur
        for i in range(SIZE-1):
            ctr=0
            for j in range(TIME-2):
                if a[(i+1)][(j+2)]>a[(i+1)][(j+1)] and a[(i+1)][(j+2)]>a[(i+1)][(j+3)]:
                    ctr=ctr+1
                    occur[(j+2)][(i+1)]=1
                    maxima[(i+1)].append((j+2))
            times_occur[ctr].append((i+1))
    def dsu(self):
        global times_occur,occur,ts,parent
        for i in range(1,TIME+1):
            sz=len(times_occur[(i)])
            for j in range(0,sz):
                particle=times_occur[(i)][j]
                for k in range(1,TIME+1):
                    if occur[(k)][particle]!=0:
                        ts[particle]+=str(k)
            for k in range(0,sz):
                for l in range(k+1,sz):
                    if str(ts[times_occur[(i)][k]])==str(ts[times_occur[i][l]]):
                        parent[times_occur[(i)][l]]=parent[times_occur[(i)][k]]

#CLASS PARTICLES FINISHED


obj1=particles()

print "Processing....."

#PLOTTING CLASS DEFINED

class plotCluster:    
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000))
    line, = ax.plot(0, 0, lw=2)
    
    # initialization function: plot the background of each frame
    def init():
        line.set_data([], [])
        self.ax.set_autoscaley_on(True)
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        #fig=plt.figure()
        global obj1,SIZE,vis,parent,ts
        
        obj1.initi()
        obj1.fill()
        obj1.analyze()
        obj1.dsu()
        plt.clf()
        ax = plt.axes(xlim=(0, SIZE+1), ylim=(-1, SIZE+1))
        line, = ax.plot(0, 0, lw=2)

        # for k in range (0,20):
        #     self.parent.append(randint(0,5))
        parent.sort()
        pos=1
        ctr=1
        l=1  
        #plt.plot(x,x,'.')  
        while l<=SIZE:
            px=[]
            py=[]
            if(parent[l]==parent[l-1]):
                while l<SIZE and parent[l]==parent[l-1]:
                    ctr=ctr+1
                    l=l+1

            apos=0      
            for j in range (pos,pos+ctr):
                for k in range (pos,pos+ctr):
                    px.append(j)
                    py.append(k)
            plt.plot(px,py,'r') 

            pos=pos+ctr
            l=l+1
            ctr=1


        #plt.plot(x, y)
        #line.set_data(x,y)
        plt.draw()
        obj1.counter=obj1.counter+100
        # a=[]
        # for i in range(1001):
        #     a.append([])
        #     for j in range(101):
        #         a[i].append(0)
        # for i in range(1001):
        #     a.append([])
        #     for j in range(101):
        #         a[i].append(0)
        # print ts[5]
        #print a[1]
        #print ts[1]
        
        del ts[:]
        ts=["" for _ in range(0,1001)]
        del times_occur[:]
        #times_occur=[]
        for _ in range(0,TIME+1):
            times_occur.append([])
        # for i in range(TIME+1):
        #     times_occur.append(0)
        occur=[]
        for i in range(0,101):
            occur.append([])
            for j in range(0,1001):
                occur[i].append(0)
        for i in range(1,SIZE+1):
            a[i][0]=a[i][TIME];
        
        print obj1.counter
        return line,


    anim = animation.FuncAnimation(fig, animate,
                                   frames=200, interval=40, blit=True)



    plt.show()



