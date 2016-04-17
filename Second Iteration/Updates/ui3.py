from Tkinter import *
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from random import randint
import random
import tkMessageBox
clicked=0

SIZE=0
e=0
MU=0

networkx=[]
networky=[]

adjacent=[]
for i in range(0,1001):
        adjacent.append([])
try:
	with open('net_adj.dat') as f:
	    for line in f: # read rest of lines
	        x,y=map(int,line.split())
	        adjacent[x].append(y)
	        networkx.append(x)
	        networky.append(y)
except Exception, e:
    print ("Network File Not Found! Place the file with proper name and run the program again")
    sys.exit() 

# MU=2
# e=0.8
# SIZE=1000
def onpick1(mouseevent):
	print("works :",mouseevent.xdata,mouseevent.xdata)
TIME=100
parent=[]
occur=[]
a=[]
prev=[]
times_occur=[]
ts=["" for _ in range(0,1001)]
maxima=[]
clusterInfo=[]

for i in range(0,1001):
	clusterInfo.append([])
	for j in range(0,1001):
		clusterInfo[i].append(" ")

for k in range(1,SIZE+2):
	parent.append(0)
class particles(object):

    #INITIALIZATION OF ARRAYS
    for i in range(1001):
        a.append([])
        prev.append([])
        for j in range(101):
            a[i].append(i/float(2001))
    
  
    
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
        #parent.append(0)
        vis.append(0)
    

    for _ in range(0,TIME+1):
        times_occur.append([])
        

    # for i in range(TIME+1):
    #     times_occur.append(0)

    #INITIALIZATION COMPLETE

    #COMPUTING FUNCTIONS DEFINED
    
	def initi(self):
	    global SIZE,parent
	    for i in range(1,SIZE+1):
	        parent[(i)]=i
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
                    add=add+(self.func(a[adjnode][j]))
                if ctr>0:
                	add=(e*add)/float(ctr)
                
                #print add
                a[i][j+1]=a[i][j+1]+add
                

    def analyze(self):
        global SIZE,a,occur,maxima,times_occur
        for i in range(SIZE):
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
                    if str(ts[times_occur[(i)][k]])==str(ts[times_occur[i][l]]) and len(str(ts[times_occur[(i)][k]]))!=0:
                        parent[times_occur[(i)][l]]=parent[times_occur[(i)][k]]
                        #print str(ts[times_occur[(i)][k]])
                        #print str(ts[times_occur[i][l]])

#CLASS PARTICLES FINISHED


obj1=particles()

top = Tk()
top.title("Cluster Visualizer")
top.minsize(400,350)

var = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()
size = StringVar()
ep = StringVar()
mu = StringVar()
btnText=StringVar()
points=StringVar()

label = Label( top, textvariable=var,font="helvetica 14" ,pady=30).grid(row=0,column=0)

var.set("Enter Number of Nodes")

#label.pack()

E1 = Entry(top, bd =2,relief=RIDGE,textvariable=size).grid(row=0,column=1)


#E1.pack()

label2 = Label( top, textvariable=var2,font="helvetica 14" ,pady=30).grid(row=01,column=0)


var2.set("Enter Value of e")
#label2.pack()

E2 = Entry(top, bd =2,relief=RIDGE,textvariable=ep).grid(row=01,column=01)


#E2.pack()

label3 = Label( top, textvariable=var3,font="helvetica 14" ,pady=30).grid(row=02,column=0)


var3.set("Enter value of Mu")
#label3.pack()

E3 = Entry(top, bd =2,relief=RIDGE,textvariable=mu).grid(row=02,column=01)

var4.set("Enter space separated list of required point")

label4 = Label( top, textvariable=var4,font="helvetica 14" ,pady=30).grid(row=03,column=0)


E4 = Entry(top, bd =2,relief=RIDGE,textvariable=points).grid(row=03,column=01)


#E3.pack()

def add():
	global SIZE,e,MU,clicked
	# if clicked==0:
	# 	btnText.set("Exit")
	# 	clicked=1
	# else:
	# 	quit()	
	tkMessageBox.showinfo("Alert","Please Place the appropriate adjacency matrix file in the same folder as this file and name it net_adj.dat")
	
	#print "Enter The No. of Nodes"
	SIZE=int(size.get())

	#print "Enter The Value of e"
	e=float(ep.get())

	#print "Enter The Value of Mu"
	MU=float(mu.get())
	
	while SIZE<0 or SIZE>1000:
	    tkMessageBox.showinfo("Invalid Input!","Invalid number of Nodes(Out of bound 1-1000). Please Enter again!")
	    clicked=0
	    return

	while e>1 or e<0:
	    tkMessageBox.showinfo("Invalid Input!","Invalid value of e(0 to 1). Please Enter again!")
	    clicked=0
	    return

	while MU<0:
	    tkMessageBox.showinfo("Invalid Input!","Invalid value of Mu (Mu > 0). Please Enter again!")
	    clicked=0
	    return
	for k in range(1,SIZE+2):
		parent.append(0)
	print "Processing....."

	#PLOTTING CLASS DEFINED
	
	class plotCluster:    
	        fig = plt.figure()
	        ax = plt.axes(xlim=(0, 1000), ylim=(0, 1000))
	        line = ax.plot(0, 0, lw=2,picker=True)
	        
	        # initialization function: plot the background of each frame
	        def init():
	            line.set_data([], [])
	            self.ax.set_autoscaley_on(True)
	            return line

	        # animation function.  This is called sequentially
	        def animate(i):
	            #fig=plt.figure()
	            global obj1,SIZE,vis,parent,ts,occur,clusterInfo
	            
	            obj1.initi()
	            obj1.fill()
	            obj1.analyze()
	            obj1.dsu()
	            plt.clf()
	            ax = plt.axes(xlim=(0, SIZE+1), ylim=(-1, SIZE+1))
	            line = ax.plot(0, 0, lw=2,picker=True)

	            # for k in range (0,20):
	            #     self.parent.append(randint(0,5))
	            
	            pos=1
	            ctr=1
	            l=1
	            marked=[];
	            for p in range(0,SIZE+1):
	                marked.append(0)
	            #NEW PLOT METHOD
	            tempx=[]
	            tempy=[]
	            for p in range(1,SIZE+1):
	                
	                for node in range(1,SIZE+1):
	                    if parent[p]==parent[node] and marked[node]==0 and parent[p]!=0 and node!=p:
	                        tempx.append(p)
	                        tempy.append(node)
	                        # tempy.append(p)
	                        # tempx.append(node)
	                        #marked[node]=1
	            #print tempx
	            #print tempy
	            #print parent
	            df=1
	            for k in range(1,SIZE+1):
	                group=[]
	                plotx=[]
	                ploty=[]
	                for j in range(1,SIZE+1):
	                    if parent[j]==k:
	                        group.append(j)
	                gsize=len(group)
	                if gsize>1:
	                    #print group
	                    gsize=gsize
	                for pl in range(0,gsize):
	                    for ql in range(0,gsize):
	                        plotx.append(df+pl)
	                        ploty.append(df+ql)
	                        clusterInfo[df+pl][df+ql]=str(group)
	                df=df+gsize
	                plt.plot(networkx,networky,'.',color="blue")
	                plt.plot(plotx, ploty,'o',color="black",mfc='None',picker=2)
	                #print ploty[0]
	                #


	            #plt.plot(tempx,tempy,'.',color="black")  
	            totalpts=0
	            #FIRST ITERATION PLOT METHOD
	            # parent.sort()  
	            # while l<=SIZE:
	            #     px=[]
	            #     py=[]
	                
	            #     if(parent[l]==parent[l-1]):
	            #         while l<SIZE and parent[l]==parent[l-1] and parent[l]!=0:
	            #             ctr=ctr+1
	            #             #print a[l]
	            #             l=l+1

	            #     apos=0
	            #     totalpts=totalpts+ctr     
	            #     for j in range (pos,pos+ctr):
	            #         for k in range (pos,pos+ctr):
	            #             px.append(j)
	            #             py.append(k)
	            #     plt.plot(px,py,'.',color="blue") 

	            #     pos=pos+ctr
	            #     l=l+1
	            #     ctr=1

	            print a[1]
	            print a[30]
	                        
	            plt.draw()
	            if(obj1.counter==100):
	                obj1.counter=100
	                #quit()
	            obj1.counter=obj1.counter+100
	            # for var in range(1,100):
	            #     print parent[var]

	            

	            
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
	            return line

		def onpick1(event):
		    thisline = event.artist
		    global clusterInfo
		    xdata =(thisline.get_xdata())
		    ydata =(thisline.get_ydata())
		    ind = event.ind
		    tkMessageBox.showinfo("Cluster",clusterInfo[xdata[ind]][ydata[ind]])
		    print clusterInfo[xdata[ind]][ydata[ind]]

	        anim = animation.FuncAnimation(fig, animate,
	                                       frames=200, interval=5000, blit=True)
	        fig.canvas.mpl_connect('pick_event', onpick1)
	        plt.show()

btnText.set("Plot Cluster")
def series():
	plt.figure(1)
	"""fig=plt.figure()
	ax1=plt.axes(xlim=(0, 100), ylim=(0, 40))
	line, = ax1.plot(0, 0, lw=2)
	color = 'o'"""
	pts=map(int,points.get().split())
	xar=[]
	for time in range(1,101):
		xar.append(time)
	#ob1=particle() 
	#def animate(i):
	global k,SIZE,TIME,a
	#obj1.fill()
	#plt.clf()
	#print i*100
	for pt in range(0,len(pts)):
		temp=[]
		for t in range(0,100):
			temp.append((a[pts[pt]][t+1]))
		if(pt<2):
			plt.subplot(211)
			plt.plot(xar, temp,'r')
			plt.plot(xar, temp,marker='o',mfc='None')
		if(pt>=2):
			plt.subplot(212)
			plt.plot(xar, temp,'r')
			plt.plot(xar, temp,marker='o',mfc='None')

			# for i in range(1,SIZE+1):
		# 	a[i][0]=a[i][TIME]
		# print a[pt][1:101]

	#ani=animation.FuncAnimation(fig,animate,frames=200,interval=100)
	plt.show()
B = Button(top, textvariable =btnText,font="helvetica 14",foreground="white" ,command = add,pady=8,background="#21A0EA").grid(row=4,column=0)
B2= Button(top, text="Plot Time series",font="helvetica 14",foreground="white" ,command = series,pady=8,background="#21A0EA").grid(row=4,column=1)

#B.pack()


top.mainloop()




#OLD TIME SERIES FUNCTION

# def series():
# 	fig=plt.figure()
# 	ax1=plt.axes(xlim=(0, 100), ylim=(0, 40))
# 	line, = ax1.plot(0, 0, lw=2)
# 	color = 'o'
# 	pts=map(int,points.get().split())
# 	xar=[]
# 	for time in range(1,101):
# 		xar.append(time)
# 	#ob1=particle() 
# 	def animate(i):
# 	    global k,SIZE,TIME,a
# 	    #obj1.fill()
# 	    plt.clf()
# 	    #print i*100
# 	    ax1 = plt.axes(xlim=(0, 100), ylim=(-1,(len(pts)+1)*10))
# 	    for pt in range(0,len(pts)):
# 	    	temp=[]
# 	    	for t in range(0,100):
# 	    		temp.append((a[pts[pt]][t+1]*5)+pt*10)
# 	    	ax1.plot(xar, temp,'r')
# 	    	ax1.plot(xar, temp,marker='o',mfc='None')

# 		# for i in range(1,SIZE+1):
# 		# 	a[i][0]=a[i][TIME]
# 		# print a[pt][1:101]






