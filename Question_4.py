
from random import random

values = [random() for i in range(20)]
x = random()

values.sort()

# find all indices where values[i] >= x
indices = []
for i in range(len(values)):
    if values[i] >= x:
        indices.append(i)

# print the sorted list and x
print("Sorted values:", values)
print("x:", x)

#  print the first matching index (if it exists)
if len(indices) > 0:
    print("First matching index:", indices[0])
else:
    print("No values are >= x")
