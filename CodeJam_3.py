#!/usr/bin/env python
# coding: utf-8

# In[12]:


t1=int(input())
def key0(item):
    return item[0]
def key2(item):
    return item[2]

list1=[]
list2=[]
for i in range(t1):
    n=int(input())
    list1.clear()
    for x in range(n):
        list2=[]
        list2=[int(a) for a in input().split(" ")]
        list2.append(x)
        list1.append(list2)
    list1.sort(key=key0)
    c=-1
    j=-1
    flag=True
    for a in list1:
        t1=a[0]
        t2=a[1]
        if c==-1:
            c=t2
            a.append('C')
        elif t1>=c:
            c=t2
            a.append('C')
        elif t1<c and t1>=j:
            j=t2
            a.append('J')
        elif t1<c and t1<j:
            flag=False
            break
    if flag==False:
        str1="IMPOSSIBLE"
    else:
        str1=""
        list1.sort(key=key2)
        str1=str1.join([a[3] for a in list1])
    print("case #{}: {}".format(i+1,str1))
  


# In[ ]:





# In[ ]:




