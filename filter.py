import time
print(time.gmtime())
readf = open('users.txt', 'r')
writef = open('users.txt', 'w')

filelines = readf.readlines()

for line in filelines:
    f = line.replace("//scratch.mit.edu/users/", "")
    f = f.replace("https:", "")
    f = f.replace("http:", "")
    f = f.replace("/", "")