fibonacci=[0,1]
a=0
b=1
tot=0
n=int(input("informe um numero inteiro ")) 
for c in range (n):
    tot=a+b
    a=b
    b=tot
    fibonacci.append(tot)
if n in fibonacci:    
    print(n," pertence a sequencia fibonacci")
else:
      print(n," NAO pertence a sequencia fibonacci")