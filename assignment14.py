
#1
f1=open("file1.txt","r")
i=0
n=int(input("Enter n\n"))
for line in f1:
    i+=1
f1.seek(0)

for j in xrange(i,0,-1):
    if(j<=n):
        print(f1.readline())
        continue
    f1.readline()
f1.close()
#2
f2=open("file1.txt","r")
lis=f2.readlines()
counter=0
for k in range(0,len(lis)):
    templist=lis[k].split(" ")
    counter+=len(templist)
print "Frequency : ",counter
f2.close()

#3
f1=open("file1.txt","r")
f2=open("file2.txt","w")
f3=open("file2.txt","r")
for line in f1:
    f2.write(line)
s=f3.readlines()
f1.close()
f2.close()

#4

f1=open("file1.txt","r")
f2=open("file2.txt","r")
f3=open("file5.txt","w")

i=0
for line in f1:
    l=f2.readline()
    f3.write(line)
    f3.write(l)
f1.close()
f2.close()
f3.close()



#5
import random
with open("file3.txt","w") as f:
    for i in range(int(input("how many random num?"))):
        line= str(random.randint(1,100))
        f.writelines(line+'\n')
        print(line)
with open("file3.txt") as f3 ,open("file4.txt","w") as f4:
    lines=f3.read().splitlines()
lines.sort()
for l in lines:
    f4.write(str(l)+'\n')