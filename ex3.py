b=1
c=1
c1=3
d=0
d1=4
e=1
f=2
print("a) ",end=" ")
for x in range (10):
    if x%2!=0:
        print(x,end=",")
print("")
print("b) ",end=" ")
for cc in range (7):
    b+=b

    print(b,end=",")

print("")
print("c) ",end=" ")

for ccc in range (8):  
    if ccc != 0 and ccc != 1:
        c+=c1
        c1+=2
        print(c,end=",")
        
    else:
        print(ccc,end=",")

print("")
print("d) ",end=" ")

for xx in range (5):
    d+=d1
    d1+=8
    print(d,end=",")

print("")
print("e) ",end=" ")

e1=[0]
for z in range (7):
    e+=e1[z-1]
    e1.append(e)
    print(e,end=",")

print("")

#numeros que começam com a letra D 
print("f) 2,10,12,16,17,18,19,200")




