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
lst2 = []
readf = open('./users.txt','r')
for line in readf:
    for item in lst2:
        if line == item:
            print("dupe found")
        else:
            lst2.append(item)

f = open('./users.txt','w')
for line in lst2:
    f.write(line)
f.close()
