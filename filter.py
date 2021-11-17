import time
print(time.gmtime())
readf = open('users.txt', 'r')
writef = open('users.txt', 'w')

filelines = readf.readlines()
nfilelines = set(())
for line in filelines:
    f = line.replace("//scratch.mit.edu/users/", "")
    f = f.replace("https:", "")
    f = f.replace("http:", "")
    f = f.replace("/", "")
    nfilelines.add(f)

writef.write(nfilelines)
