n = int(input())

i = 1
j = 1

for i in range(1,n+1):
    for j in range (1,n+1):
        if j == n and i != n:
            ending = "\n"
        else:
            ending = " "
        if i == 1 or j == 1 or i == n or j == n:
            print ("*", end = ending)
        else:
            print ("@", end = ending)
        j +=1
    i += 1