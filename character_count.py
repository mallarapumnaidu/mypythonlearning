inputval = input("enterinput values:")

print(type(inputval))
print(inputval)
key = []
cnt = []
j = None
x = 0

for i in inputval:


    if j == i or j == None:
        j = i
        x = x+1
        #print (j,x)

    else:
        key.append(j)
        cnt.append(x)
        x = 1
        j = i

key.append(j)
cnt.append(x)

for a,b in zip(key,cnt):
    print(a,b)
