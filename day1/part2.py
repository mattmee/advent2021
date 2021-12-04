a = b = c = 0
increase = -3

with open('input') as file:
    for line in file:
	current = int(line)
	if  a+b+c < b+c+current:
       	    increase += 1
	a = b
	b = c
	c = current

print(increase)
