#!/usr/bin/python

from functools import reduce
from operator import mul

def answer(xs):
	no_zero = [x for x in xs if x != 0]
	product = reduce(mul, no_zero)
	if len(no_zero) <= 1:
		return max(xs)
	if product > 0:
		return product
	else:
		return product/max([x for x in xs if x < 0])