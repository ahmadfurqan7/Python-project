#find file for word count
f=open("file-directory.txt","r")
#change directory file from your computer
#ex: "D://folder/file.txt"

#list all word from file
c=[]
for x in f:
    print(x)
    c.append(x.split(' '))

#count word form len of the list
d=0
for i in range(len(c)):
    d=d+1
print(d)
