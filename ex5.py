list=[]
write=(str(input("digite algo e os carcteres serão invertidos \n")))
list.append(write)
letters=list[0]

for c in range(len(letters)-1,-1,-1):
    print(letters[c],end="")

