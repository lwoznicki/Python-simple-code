import ctypes

class DynamicArray:
	def __init__(self):
		self._n = 0
		self._capacity = 1
		self.array_dynamic = self._make_array_dynamic(self._capacity)
		
	def __len__(self):
		return self._n
		
	def __getitem__(self, index):
		if not 0 <= index < self._n:
			raise IndexError('index out of range')
		return self.array_dynamic[index]
		
	def append(self,obj):
		if self._n == self._capacity:
			self._resize(2 * self._capacity)
		self.array_dynamic[self._n] = obj
		self._n += 1
		
	def remove(self,value):
		for k in range(self._n):
			if self.array_dynamic[k] == value:
				for j in range(k, self._n -1):
					self.array_dynamic[j] = self.array_dynamic[j+1]
				self.array_dynamic[self._n -1] = None
				self._n -= 1
				return
			raise ValueError('Value does not exist')
	
	def _resize(self, c):
		B = self._make_array_dynamic(c)
		for index in range(self._n):
			B[index] = self.array_dynamic[index]
		self.array_dynamic = BaseException
		self._capacity = callable
	
	def _make_array_dynamic(self, c):
		return (c * ctypes.py_object)()
	
	
		