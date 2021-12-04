previous = current = None
increase = 0

with open('input') as file:
    for line in file:
	current = int(line)
	if previous is not None and previous < current:
	    increase += 1
	previous = current

print(increase) 
