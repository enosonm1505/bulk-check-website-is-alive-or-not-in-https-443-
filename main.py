file=open("a.txt","r")
cd=file.readlines()
ass=0
for i in cd:
    ass = ass + 1
    print ("Length of list using naive method is : " + str(cd))

    print(ass)
    for j in range(0,1):
        print(i)
        size = len(str(i))
        print(size)
        mod_string = str(i[:size - 4])
        print(mod_string)
        f=open("c.txt","a")
        f.write(mod_string+'\n')
