file=open('countries.txt','r')
print(file.readable())
#print(file.readline()) # read first line
# print(file.readlines())

for lines in file.readlines():
    print(lines)
file.close()

# r-- read
# w-- write
# a-- append
# r+-- to do both write and read
