import sys
input = sys.stdin.readline
from collections import deque

gear = [deque()]
for _ in range(4):
    gear.append(deque(map(int, input().strip())))

def rotate_left(num, dir):
    if num == 1:
        return
    if gear[num][6] != gear[num - 1][2]:
        rotate_left(num - 1, -dir)
        gear[num - 1].rotate(-dir)

def rotate_right(num, dir):
    if num == 4:
        return
    if gear[num][2] != gear[num + 1][6]:
        rotate_right(num + 1, -dir)
        gear[num + 1].rotate(-dir)

k = int(input())
for _ in range(k):
    num, direction = map(int, input().split())
    rotate_left(num, direction)
    rotate_right(num, direction)
    gear[num].rotate(direction)

score = 0
if gear[1][0]: score += 1
if gear[2][0]: score += 2
if gear[3][0]: score += 4
if gear[4][0]: score += 8
print(score)
