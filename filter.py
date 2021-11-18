readf = open('./users.txt','r')
a = ['//scratch.mit.edu/users/','https:','http:', "/"]
lst = []
for line in readf:
    for word in a:
        if word in line:
            line = line.replace(word,'')
    lst.append(line)
readf.close()
f = open('./users.txt','w')
for line in lst:
    f.write(line)
f.close()
