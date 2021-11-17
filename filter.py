import time
y = time.gmtime()
readf = open('users.txt', 'r')
writef = open('users.txt', 'w')
print(y)
filelines = readf.readlines()
nfilelines = set(())
for line in filelines:
    f = line.replace("//scratch.mit.edu/users/", "")
    f = f.replace("https:", "")
    f = f.replace("http:", "")
    f = f.replace("/", "")
    if not f in nfilelines:
        nfilelines.add(f)

writef.write(nfilelines)
writef.close()
readf.close()
print(time.gmtime())
