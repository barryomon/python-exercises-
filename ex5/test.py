
var = open("test.py", "r")
count = 0 

for line in var:
    count = count + 1

print("Line Count: ", count)



Var = open('test.py')
inp = Var.read()
print(len(inp))
print(inp[:20])