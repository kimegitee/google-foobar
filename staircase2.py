'''
Alternative solution to The Grandest Staircase Of Them All
'''

def answer(n):
	return moarstairs(n, 1) - 1

class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result

@memoize
def moarstairs(n, lowerbound):
	if n == 0:
		return 1
	if n < lowerbound:
		return 0
	return sum(moarstairs(n-x, x+1) for x in range(lowerbound, n+1))