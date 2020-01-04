import random

begin = 1
end = 10000
limit = 1000

RandomListOfIntegers = [random.randint(begin, end) for iter in range(limit)]

print(RandomListOfIntegers)