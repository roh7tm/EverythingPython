import sys

n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

print(height)

height.sort()
height.reverse()

print(height)
c = 0
if height[0] == height[1]:
    c = 2

if height[0] == height[1] == height[2]:
    c = 3

if height[0] != height[1]:
    c = 1

print(c)

