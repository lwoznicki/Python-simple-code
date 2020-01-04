class Stack:
	def __init__(self):
		self.dataStack = []
		
	def __len__(self):
		return len(self.dataStack)
		
	def is_empty(self):
		return len(self.dataStack) == 0
		
	def push(self, e):
		self.dataStack.append(e)
		
	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self.dataStack[-1]
		
	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self.dataStack.pop()
		
stack = Stack()

stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
print(stack.top())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
#End of data
#print(stack.pop())
