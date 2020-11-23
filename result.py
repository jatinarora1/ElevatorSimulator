from elevator import ele

e = ele()


# In this case at one time only one floor is selected
# But it is possible that more than one number of floors can be selected at the same time
# For that we can do one thing just call the e.call() function and then call e.run_until_stopped() function for that.
direction = 1
print('Enter dest_floor',)
floor = int(input())
e.call(floor,direction)
e.run_until_stopped()
while True:
	print('Enter direction and dest_floor')
	direction, dest_floor = input().split()
	if(direction == 'q'): exit()
	direction = int(direction)
	dest_floor = int(dest_floor)
	e.call(dest_floor,direction)
	e.run_until_stopped()


