def changeDepth(direction, value, depth):
    value = int(value)
    if direction == 'up':
	return depth - value
    return depth + value
    
def changeHorizontal(direction, value, horizontal):
    value = int(value)
    if direction == 'forward':
        return horizontal + value
    return horizontal - value

horizontal = 0
depth = 0

with open('input') as file:
    for line in file:
	action, value = line.split(' ')
	if action == 'forward':
	    horizontal = changeHorizontal(action, value, horizontal)
	else:
	    depth = changeDepth(action, value, depth)

print(horizontal * depth)
