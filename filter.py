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
print(nfilelines)
for line in nfilelines:
    if not newlines.index(line) > 0:
        newlines.append(line)
lts = ""
for line in newlines:
    lts = lts + line
writef.write(lts)
writef.close()
readf.close()
print(time.gmtime())
