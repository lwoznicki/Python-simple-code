https://www.hackerrank.com/challenges/py-check-subset/problem

for i in range(int(input())):
    a = int(input())
	A_set = set(input().split()) 
    b = int(input()) 
	B_set = set(input().split())
    print((A_set & B_set) == A_set)