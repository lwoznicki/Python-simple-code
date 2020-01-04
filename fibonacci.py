def fibonacci(howManyNumbers):
	a = 0
	b = 1
	counter = 0
	while counter < howManyNumbers :
		nextValue = a + b
		a = b
		b = nextValue	
		counter += 1
		print(a)
		
#Use function
fibonacci(400)
