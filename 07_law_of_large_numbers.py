import numpy as np
from numpy.random import randn

# specify sample size
#N = 10
N = 100
#N = 1000

# reset counter
counter = 0

for i in range(N):
    x = randn()
    if x >= -1 and x <= 1:
        counter = counter + 1
answer = counter / N
print(counter, "of out", N)
print("percentage", answer)


# Other way to do it
counter = 0
answer = 0
for j in randn(N):
    if (j >= -1 and j <= 1):
        counter = counter + 1
answer = counter / N
print(counter, "of out", N)
print("percentage", answer)

