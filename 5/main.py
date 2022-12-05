#!/usr/bin/env python

# https://adventofcode.com/2022/day/5

f = open("input.txt", 'r')

lines = f.read().split('\n')
stacks = [[stack][0] for stack in [[line[i] for line in lines if len(line) > i and line[i].isupper()] for i in range(50)] if stack]
instructions = [[int(word) for word in line.split(' ') if word.isnumeric()] for line in lines if len(line) > 1 and line[0].islower()]

for instruction in instructions:
    for i in range(instruction[0]):
        stacks[instruction[2]-1].insert(0, stacks[instruction[1]-1].pop(0))

tops = [stack[0] for stack in stacks]

print("".join(tops))
