f = open('DataFile', 'r')
# print(f.readline()) # will read line 1 and pointer will move to next line
# print(f.readline(4)) # will read only first 4 chars of line and pointer will move to 5th char
# print(f.readline())
# print(f.readline())


f1 = open('DataFile2', 'w')  # will check if file is present else will create new file, overwrite the data
f1.write('something')
f1.write('useful')
f1.write('laptop')

f2 = open('DataFile2', 'a')  # append file
f2.write('  append something')

for data in f:
    f2.write(data)

# below will make a copy of pic , rb is read binary and wb is write binary , pics are in binary format
pic = open('MyPic.JPG', 'rb')

pic_copy = open('NewCopy.JPG', 'wb')

for i in pic:
    pic_copy.write(i)
