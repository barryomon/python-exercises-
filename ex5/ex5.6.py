

fname = input("enter file name :")

for line in open(fname):
    line = line.rstrip()
    if line .startswith("X-DSPAM-Confidence:"):
        num = float(line.split(':')[1])
        print(num)