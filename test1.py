# Open the file with read only permit
fh = open('list1', "r")
s1=''
s2=''
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
for line in fh:
    # in python 2
    # print line
    # in python 3
    s1=line
    if s1!=s2:
    	print(line)
    s2=s1	
fh.close()
# close the file after reading the lines.

