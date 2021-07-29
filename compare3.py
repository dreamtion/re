
for line1 in open('list3','r'):
    i=0
    for line2 in open('list3','r'):
        if line1 == line2: 
           i=i+1
    if i>1:
       print(line1)
       print (i)
