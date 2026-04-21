import re 


fname = open('regex_sum_2397086.txt', 'r')
count =[]
for line in fname :
    line = line.strip()
    line = re.findall('[0-9]+', line)
    if len(line) > 0 :
        for line in line :
            line = int(line)
            count.append(line)
        
         

print(sum(count))
