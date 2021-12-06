def changeDepth(direction, value, aim):
    value = int(value)
    if direction == 'up':
	return aim - value
    return aim + value
    
def changeHorizontal(direction, value, horizontal, aim, depth):
    value = int(value)
    if direction == 'forward':
        return horizontal + value, depth + aim * value
    return horizontal - value

aim = 0
horizontal = 0
depth = 0

with open('input') as file:
    for line in file:
	action, value = line.split(' ')
	if action == 'forward':
	    horizontal, depth = changeHorizontal(action, value, horizontal, aim, depth)
	else:
	    aim = changeDepth(action, value, aim)

print(horizontal * depth)
