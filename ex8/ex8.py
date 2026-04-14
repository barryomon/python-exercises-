

fname = input("enter file name ")
fhandle = open(fname)
for file in fhandle:
    if file.startswith('From'):
     count = count + 1
     file = file.split()
     print(file[1])
     print(count)