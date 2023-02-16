import math
import statistics
f=open("data.txt","r")
lines = f.readlines()
value=[]
d=[]

for line in lines:
    a=line.split(",")
    'b=[float(x) for x in a]'
    value.append(a)
print ("The data points are: ",value)
row=len(value)
col=len(value[0])

print("Row:",row)
print("Col:",col)


'class'

clas=[]
for x in range(row):
    clas.append(value[x][col-1])
print("Class label: ",clas)

'data'

data=[]

for x in range(row):
    rowd=[]
    for y in range(col-1):
       b=value[x][y]
       rowd.append(float(b))
    data.append(rowd)
print(data)

data_row=len(data)
data_col=len(data[0])
print("Data row:",data_row)
print("Data col:",data_col)


'query'

q=[]
for x in range(data_col):
    c=float(input("enter the values: "))
    q.append(c)
print("Query: ",q)


'distance'

for i in range(data_row):
    d1=0
    for j in range(data_col):
        d1=d1+((data[i][j]-q[j])**2)
        d2=math.sqrt(d1)
        d3=round(d2,3)
    d.append(d3)
print("Distance: ",d) 


k=int(input("Enter k value: "))
print("K value:",k)

dd=d.copy()
d.sort()
print("Original sorted: ",d)
print("Duplicate original order: ",dd)

'class order' 
qc=[]
for i in  range(k):
    ind=dd.index(d[i])
    print(ind)
    qc.append(clas[ind])
print(qc)


'''print(value[0][1]) '''
'''
col=(len(value[0]))
row=len(value)
clas=[]
for x in range(row):
    clas.append(value[x][col-1])
print("Class label: ",clas)
q=[]
for x in range(col-1):
    c=float(input("enter the values: "))
    q.append(c)
print("Query: ",q)
    
for i in range(row):
    d1=0
    for j in range(col-1):
        d1=d1+((value[i][j]-q[j])**2)
        d2=math.sqrt(d1)
        d3=round(d2,3)
    d.append(d3)
print("Distance: ",d) 
k=int(input("Enter k value: "))
dd=d.copy()
d.sort()
print("Original: ",d)
print("Duplicate: ",dd)
qc=[]
for i in  range(k):
    ind=dd.index(d[i])
    print(ind)
    qc.append(clas[ind])
print(qc)
qc.sort()
s=sum(qc)

print("Query class is:",s/k)'''