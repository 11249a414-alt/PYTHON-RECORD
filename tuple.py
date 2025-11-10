#its not coming in my file so i am doing here
from collections import namedtuple
Point=namedtuple('Point',['x', 'y'])
p= Point(10,20)
print(p.x)

from collections import defaultdict
s=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
d=defaultdict(list)
for k,v in s:
    d[k].append(v)
    print(d)



