#1
d = {'name': 'Chris', 'city': 'Seattle', 'cake': 'Chocolate'}

print d

d.pop('cake')
print d
d['fruit'] = 'Mango'
print d.keys()
print d.values()
print 'cake' in d
print 'Mango' in d.values()

#2
l1 = range(16)
l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
mydict = {}
for i, j in zip(l1, l2):
    mydict[i] = j
print mydict

#3
mydict2 = {}

for i, j in zip(d.keys(), d.values()):
    mydict2[i] = j.count('a')

#4
s2= set([2,4,6,8,10,12,14,16,18,20])
s3 = set([3,6,9,12,15,18])
s4 = set([4,8,16,20])

print s3.issubset(s2)
print s4.issubset(s2)

#5
s = set(['P','y','t','h','o','n'])
s.add('i')
print s
fs = frozenset(('m','a','r','a','t','h','o','n'))
print s.union(fs)
print s.intersection(fs)
