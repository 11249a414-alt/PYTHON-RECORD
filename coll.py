from collections import deque
d = deque([1, 2, 3])
print(d)
d.appendleft(4) # deque([0, 1, 2, 3])
print(d)
d.pop() # 3, d is now deque([0, 1, 2])
print(d)


