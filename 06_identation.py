import numpy as np
from numpy.random import randn

answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
    
print(x)
print(answer)
    
answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
else:
    answer = "Less than 1"
    
print(x)
print(answer)
    
# Nested Statements    
answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
else:
    if x >= -1:
        answer = "Between -1 and 1"
    else:
        answer = "Less than -1"
    
print(x)
print(answer)

# Chained Statements    
answer = None
x = randn()
if x > 1:
    answer = "Greater than 1"
elif x >= -1:
    answer = "Between -1 and 1"
else:
    answer = "Less than -1"
    
print(x)
print(answer)

