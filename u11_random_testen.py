from random import random

cnt = 0

for i in range(1000000):
    if random() < 0.42:
        cnt += 1

print(cnt)