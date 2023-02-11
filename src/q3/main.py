from rule import *

inp_file = open('q3/config.txt','r')
lines_read = inp_file.readlines()


lists=[]

for line in lines_read:
    col=[]
    r = line.split()
    lists.append(r)

a = int(lists[0][0])
b = int(lists[0][1])
c = int(lists[0][2])

l1 = []
for i in range(0,b):
	col = []
	for j in range(0,a):
		col.append(0)
	l1.append(col)

for x in range(1,c+1):
    j = int(lists[x][0])
    i = int(lists[x][1])
    l1[b-i][j-1] = 1

l3 = []
for i in range(0,b):
	col = []
	for j in range(0,a):
		col.append(l1[i][j])
	l3.append(col)

count = 0
print()
print("Initial State:")
print()
for m in range(0,b):
        for n in range(0,a):
            if(l1[m][n]==1):
                print("X",end="")
            else:
                print("O",end="")
        print()

print()

while(1):
    iterations = int(input("Number of iterations from Current State: "))
    
    count = count + iterations

    while(iterations>0):
        l2 = []
        for i in range(0,b):
            cl_vec=[]
            for j in range(0,a):
                nb=[]

                if(i+1<b):
                    nb.append(l1[i+1][j])            # top

                    if(j+1<a):
                        nb.append(l1[i+1][j+1])      # top right  

                    else:
                        nb.append(0)

                else:
                    nb.append(0)
                    nb.append(0)

                
                if(i-1>=0):
                    nb.append(l1[i-1][j])            # bottom       

                    if(j-1>=0):
                        nb.append(l1[i-1][j-1])      # bottom left

                    else:
                        nb.append(0)

                else:
                    nb.append(0)
                    nb.append(0)
                if(i+1<b):


                    if(j-1>=0):
                        nb.append(l1[i+1][j-1])      # top left

                    else:
                        nb.append(0)

                else:
                    nb.append(0)

                if(i-1>=0):
                    

                    if(j+1<a):
                        nb.append(l1[i-1][j+1])      # bottom right

                    else:
                        nb.append(0)

                else:
                    nb.append(0)
                    

                if(j+1<a):
                    nb.append(l1[i][j+1])            # right 

                else:
                    nb.append(0)
                    

                if(j-1>=0):
                    nb.append(l1[i][j-1])            # left

                else:
                    nb.append(0)

                tmp = rule3(l1[i][j],nb)

                # if(tmp==1):
                #     cl_vec.append(1)
                # else:
                #     cl_vec.append(l1[i][j])

                cl_vec.append(tmp)
            l2.append(cl_vec)

        iterations = iterations -1

        for i in range(0,b):
            for j in range(0,a):
                l1[i][j] = l2[i][j]

    if(iterations==-1):
        break
    print()
    # print(l1)
    print("After Iteration "+str(count)+" from Initial State:")
    print()
    for m in range(0,b):
            for n in range(0,a):
                if(l1[m][n]==1):
                    print("X",end="")
                else:
                    print("O",end="")
            print()
    print("---------------------------------------------")
    with open("q3/output.txt","w") as fw:
        for m in range(0,b):
            for n in range(0,a):
                if(l1[m][n]==1):
                    fw.write("X")
                else:
                    fw.write("O")
            fw.write("\n")

#iterations = int(input("enter the no.of iterations: "))
