
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
s=input("Give Binary Data Stream As an Input")
print(" Give Number to Perform Following Technique: ","1.NRZ-L","2.NRZ-I","3.Manchester","4.Differantial Manchester","5.AMI")
n=int(input())
if(n==1):
    print("Perform NRZ-L")
    ls=list()
    for i in range(len(s)):
        if(s[i]=='0'):
            ls.append(-1)
        else:
            ls.append(1)
    xs = np.repeat(range(len(s)), 2)
    ys = np.repeat(ls, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+1))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
    plt.step(xs,ys)
    plt.ylim(-1.5,1.5)
    plt.show() 
    ls1=list()
    for i in range(len(s)):
        if(s[i]=='0'):
            ls1.append(1)
        else:
            ls1.append(-1)
    xs1 = np.repeat(range(len(s)), 2)
    ys1 = np.repeat(ls1, 2)
    xs1=xs1[1:]
    xs1=np.append(xs1,(xs1[len(xs1)-1]+1))
    ys1=ys1[:-1]
    ys1=np.append(ys1,(ys1[len(ys1)-1]))
    plt.step(xs1,ys1)
    plt.ylim(-1.5,1.5)
    plt.show()  
elif(n==2):
    print("Perform NRZ-I")
    Is=list()
    if(s[0]=='0'):
        Is.append(-1)
    else:
        Is.append(1)
    k=len(s)
    i=1
    while(i<k):
        if(int(s[i])==0):
            Is.append(Is[i-1])
        else:
            Is.append(-Is[i-1])
        i=i+1
    xs = np.repeat(range(len(s)), 2)
    ys = np.repeat(Is, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+1))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
    plt.step(xs,ys)
    plt.ylim(-1.5,1.5)
    plt.show()
    Is=list()
    if(s[0]=='0'):
        Is.append(1)
    else:
        Is.append(-1)
    k=len(s)
    i=1
    while(i<k):
        if(int(s[i])==0):
            Is.append(Is[i-1])
        else:
            Is.append(-Is[i-1])
        i=i+1
    xs1 = np.repeat(range(len(s)), 2)
    ys1= np.repeat(Is, 2)
    xs1=xs1[1:]
    xs1=np.append(xs1,(xs1[len(xs1)-1]+1))
    ys1=ys1[:-1]
    ys1=np.append(ys1,(ys1[len(ys1)-1]))
    plt.step(xs1,ys1)
    plt.ylim(-1.5,1.5)
    plt.show()
elif(n==3):
    print("Perform Manchester")
    pm=list()
    for j in range(len(s)):
        if(s[j]=='0'):
            pm.append(-1)
            pm.append(1)
        else:
            pm.append(1)
            pm.append(-1)
    xs=[x*0.5 for x in range(0,(2*len(s)))]
    xs=np.repeat(xs,2)
    ys = np.repeat(pm, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+0.5))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
    plt.step(xs,ys)
    plt.ylim(-1.5,1.5)
    plt.show()
    pm=list()
    for j in range(len(s)):
        if(s[j]=='0'):
            pm.append(1)
            pm.append(-1)
        else:
            pm.append(-1)
            pm.append(1)
    xs1=[x*0.5 for x in range(0,(2*len(s)))]
    xs1=np.repeat(xs1,2)
    ys1= np.repeat(pm, 2)
    xs1=xs1[1:]
    xs1=np.append(xs1,(xs1[len(xs1)-1]+0.5))
    ys1=ys1[:-1]
    ys1=np.append(ys1,(ys1[len(ys1)-1]))
    plt.step(xs1,ys1)
    plt.ylim(-1.5,1.5)
    plt.show()
elif(n==4):
    print("Perform Differantial Manchester")
    pdm=list()
    pdm.append(1)
    pdm.append(-1)
    i=1
    k=len(s)
    while(i<k):
        if(int(s[i])==1):
            pdm.append(pdm[len(pdm)-1])
            pdm.append(-pdm[len(pdm)-1])
        else:
            pdm.append(-pdm[len(pdm)-1])
            pdm.append(-pdm[len(pdm)-1])
        i=i+1
    print(pdm)
    xs=[x*0.5 for x in range(0,(2*len(s)))]
    xs=np.repeat(xs,2)
    ys = np.repeat(pdm, 2)
    xs=xs[1:]
    xs=np.append(xs,(xs[len(xs)-1]+0.5))
    ys=ys[:-1]
    ys=np.append(ys,(ys[len(ys)-1]))
    plt.step(xs,ys)
    plt.ylim(-1.5,1.5)
    plt.show()
    pdm=list()
    pdm.append(-1)
    pdm.append(1)
    i=1
    k=len(s)
    while(i<k):
        if(int(s[i])==1):
            pdm.append(pdm[len(pdm)-1])
            pdm.append(-pdm[len(pdm)-1])
        else:
            pdm.append(-pdm[len(pdm)-1])
            pdm.append(-pdm[len(pdm)-1])
        i=i+1
    print(pdm)
    xs1=[x*0.5 for x in range(0,(2*len(s)))]
    xs1=np.repeat(xs1,2)
    ys1 = np.repeat(pdm, 2)
    xs1=xs1[1:]
    xs1=np.append(xs1,(xs1[len(xs1)-1]+0.5))
    ys1=ys1[:-1]
    ys1=np.append(ys1,(ys1[len(ys1)-1]))
    plt.step(xs1,ys1)
    plt.ylim(-1.5,1.5)
    plt.show()
else:
    print("0.No Scrambling","1.Scrambling")
    q=int(input())
    if(q==0):
        print("Perform AMI")
        am=list()
        m=1
        for i in range(len(s)):
            if(int(s[i])==0):
                am.append(0)
            else:
                if(m%2==1):
                    am.append(1)
                else:
                    am.append(-1)
                m=m+1
        xs = np.repeat(range(len(s)), 2)
        ys = np.repeat(am, 2)
        xs=xs[1:]
        xs=np.append(xs,(xs[len(xs)-1]+1))
        ys=ys[:-1]
        ys=np.append(ys,(ys[len(ys)-1]))
        plt.step(xs,ys)
        plt.ylim(-1.5,1.5)
        plt.show()  
        am=list()
        m=1
        for i in range(len(s)):
            if(int(s[i])==0):
                am.append(0)
            else:
                if(m%2==1):
                    am.append(-1)
                else:
                    am.append(1)
                m=m+1
        xs1 = np.repeat(range(len(s)), 2)
        ys1 = np.repeat(am, 2)
        xs1=xs1[1:]
        xs1=np.append(xs1,(xs1[len(xs1)-1]+1))
        ys1=ys1[:-1]
        ys1=np.append(ys1,(ys1[len(ys1)-1]))
        plt.step(xs1,ys1)
        plt.ylim(-1.5,1.5)
        plt.show()  
    else:
        print("Perform Scrambling")
        print("1.B8ZS","2.HDB3")
        p=int(input())
        q=len(s)
        if(p==1):
            print("Perform B8ZS")
            bz=list()
            m=1
            s1=s.replace("00000000","000vb0vb")
            for i in range(len(s1)):
                if(s1[i]=='0'):
                    bz.append(0)
                elif(s1[i]=='1'):
                    if(m%2==1):
                        bz.append(1)
                    else:
                        bz.append(-1)
                    m=m+1
                elif(s1[i]=='v'):
                    if(m%2==1):
                        bz.append(-1)
                    else:
                        bz.append(1)
                else:
                    if(m%2==1):
                        bz.append(1)
                    else:
                        bz.append(-1)
                    m=m+1
            xs = np.repeat(range(len(s)), 2)
            ys = np.repeat(bz, 2)
            xs=xs[1:]
            xs=np.append(xs,(xs[len(xs)-1]+1))
            ys=ys[:-1]
            ys=np.append(ys,(ys[len(ys)-1]))
            plt.step(xs,ys)
            plt.ylim(-1.5,1.5)
            plt.show()
            bz=list()
            m=1
            for i in range(len(s1)):
                if(s1[i]=='0'):
                    bz.append(0)
                elif(s1[i]=='1'):
                    if(m%2==1):
                        bz.append(-1)
                    else:
                        bz.append(1)
                    m=m+1
                elif(s1[i]=='v'):
                    if(m%2==1):
                        bz.append(1)
                    else:
                        bz.append(-1)
                else:
                    if(m%2==1):
                        bz.append(-1)
                    else:
                        bz.append(1)
                    m=m+1
            xs1 = np.repeat(range(len(s)), 2)
            ys1 = np.repeat(bz, 2)
            xs1=xs1[1:]
            xs1=np.append(xs1,(xs1[len(xs1)-1]+1))
            ys1=ys1[:-1]
            ys1=np.append(ys1,(ys1[len(ys1)-1]))
            plt.step(xs1,ys1)
            plt.ylim(-1.5,1.5)
            plt.show()  
        else:
            print("Perform HDB3")
            m=0
            hd=list()
            f=s.find("0000")
            if(f==-1):
                f=len(s)
            i=0
            k=len(s)
            d=1
            p=0
            while(i<k):
                if(s[i]=='1'):
                    m=m+1
                    p=p+1
                    if(m%2==1):
                        hd.append(d)
                        d=1
                    else:
                        hd.append(-d)
                        d=-d
                else:
                    if(i<f):
                        hd.append(0)
                    elif(i==f):
                        i=i+3
                        if(p%2==0):
                            hd.append(-d)
                            hd.append(0)
                            hd.append(0)
                            hd.append(-d)
                            d=-d
                            p=p+2
                            m=m+1
                        else:
                            hd.append(0)
                            hd.append(0)
                            hd.append(0)
                            hd.append(d)
                            p=p+1
                        jk=s[i+1:(i+1)+(k-i-1)]
                        x=jk.find("0000")
                        if(x==-1):
                            f=k
                        else:
                            f=i+1+x
                i=i+1
            xs = np.repeat(range(len(s)), 2)
            ys = np.repeat(hd, 2)
            xs=xs[1:]
            xs=np.append(xs,(xs[len(xs)-1]+1))
            ys=ys[:-1]
            ys=np.append(ys,(ys[len(ys)-1]))
            plt.step(xs,ys)
            plt.ylim(-1.5,1.5)
            plt.show()
            print(hd)
                
            
