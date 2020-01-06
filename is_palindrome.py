def is_palindrome(word):
	i = 0
	j = len(word) - 1
	while i < j:
		if word[i] != word[j]:
			return False
		i += 1
		j -= 1
	return True
	
print(is_palindrome('abcdedcba'))
print(is_palindrome('abc'))