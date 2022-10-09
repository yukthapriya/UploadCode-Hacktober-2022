# Online Python compiler (interpreter) to run Python online.
n=7900
f=str(n)
d = dict()

for i in f:
    count=0
    for j in f:
        if(i==j):
            count=count+1
    d[i]=count
  
s=""
for i in f:
    s=s+str(d[i])
print(s)
