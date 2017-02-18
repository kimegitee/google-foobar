#!/usr/bin/python

"""
Second Challenge For Level 2: Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------

Test cases
==========

Inputs:
    (int) src = 19
    (int) dest = 36
Output:
    (int) 1

Inputs:
    (int) src = 0
    (int) dest = 1
Output:
    (int) 3
"""

from itertools import permutations, count

def move_from(here):
	"""
	Calculates legal positions a knight can move to.

	@param here A set of 2-tuples for each x, y coordinate pair on the chessboard.
	"""
	return {(x + i, y + j) 
		for x, y in here 
		for i, j in permutations([-2, -1, 1, 2], 2)
			if abs(i) != abs(j) 
				and x + i in range(8) 
				and y + j in range(8)}

def answer(src, dest):
	visited = {convert(src)}
	for moves_made in count(0):
		if convert(dest) in visited:
			return moves_made
		else:		
			visited = move_from(visited).union(visited)

def convert(x):
	"""
	Converts a coordinate given by an int to a pair of x, y coordinates
	"""
	return divmod(x, 8)

