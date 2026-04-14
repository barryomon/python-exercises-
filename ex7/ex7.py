
#working with files and lists

words =[ ] 

fname = input("Enter file name: ")

for line in open(fname):
    line =line.split()
    for word in line:
        if word not in words:
            words.append(word)
            
words.sort()        
print(words) 



Details = {"name”: “jason”, “email” : “bb@gmail.com”}

print(Details[‘name’])