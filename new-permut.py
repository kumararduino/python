a = 999
c = 900
s = str(a)
li = []
nine = "9"
temp = ''
for i in range(1,len(s)):
    temp = temp + nine
    li.append(temp)
li = map(int,li)
li= li[::-1]
temp = []
for i in range(len(li)):
    for j in range(i+1,len(li)):
        temp.append(li[i]-li[j])
temp = sorted(temp)
temp = temp[::-1]
temp1 = []
for i in range(len(temp)):
    for j in range(i+1,len(temp)):
        temp1.append(temp[i]-temp[j])
temp1 = set(temp1)
temp1 = list(temp1)
temp2 = []
for i in temp1:
    b = str(i)
    
    for j in b:
        if j!="0" and j!= '9':
            temp2.append(i)
            break
for i in temp2:
    temp1.remove(i)
temp1 = sorted(temp1)
temp1 = temp1[::-1]
final = sorted(list(set(li+temp+temp1)))
print final[::-1]
f = []
for i in final:
    f.append(a-i)
    f.append(c+i)
f = sorted(list(set(f)))
print f[::-1]
print len(f)
