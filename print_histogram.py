def print_histogram(h):
    dict = []
    dict += sorted(h.keys())
    for e in dict:
        print(e, h[e])
		
spaghetti = {'s' : 1, 'p' : 1, 'a' : 1, 'g' : 1, 'h' : 1, 'e' : 1 ,'t' : 2 , 'i' : 1}
print_histogram(spaghetti)
