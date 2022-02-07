f=open('C:\\sub.txt','r')  #'C:\\sub.txt' this place should be replaced with the file path
a=f.readlines()
mod = []
for l in a:
    if l[:1]=='0':
        pass
    elif l[:1]=='1':
        pass

    else:

        c = open('final.text', 'a') #'final.txt' this is the new file name
        c.write(l)


c.close()


