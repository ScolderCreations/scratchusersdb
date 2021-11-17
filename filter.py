import time
y = time.gmtime()
readf = open('users.txt', 'r')
writef = open('users.txt', 'w')
print(y)
filelines = readf.readlines()
nfilelines = set(())
newlines = []
for line in filelines:
    f = line.replace("//scratch.mit.edu/users/", "")
    f = f.replace("https:", "")
    f = f.replace("http:", "")
    f = f.replace("/", "")
    if not f in nfilelines:
        nfilelines.add(f)
for line in nfilelines:
    if not line in newlines:
        newlines.append(line)
writef.write(str(newlines))
writef.close()
readf.close()
print(time.gmtime())
