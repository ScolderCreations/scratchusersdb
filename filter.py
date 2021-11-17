import time
y = time.gmtime()
readf = open('users.txt', 'r')
writef = open('users.txt', 'w')
print(y)
filelines = readf.read().split('\n')
nfilelines = set(())
newlines = []
for line in filelines:
    f = line.replace("//scratch.mit.edu/users/", "")
    f = f.replace("https:", "")
    f = f.replace("http:", "")
    f = f.replace("/", "")
    if not f in newlines:
        newlines += f
print(newlines)
lts = ""
for line in newlines:
    lts = lts + line
writef.write(lts)
writef.close()
readf.close()
print(time.gmtime())
