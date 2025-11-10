from collections import Counter
counts = Counter(['a', 'b', 'a', 'c', 'b']) # Output: Counter({'a': 2, 'b': 2, 'c': 1})
print(counts)

from collections import deque
d=deque([1,2,3])
print(d)
d.appendleft(0)
print(d)
d.pop()
print(d)