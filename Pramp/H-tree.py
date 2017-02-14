"""
Draw H-tree
https://en.wikipedia.org/wiki/H_tree#/media/File:H_tree.svg
Given a drawline method
Write a method to draw an H-tree
------------- NOT COMPLETE ----------------
"""

def drawLine(xOne, yOne, xTwo, yTwo):
    pass
	
def drawHTree(x, y, length, depth):

  if (depth == 0) return
  
  x0 = x - length/2
  x1 = x + length/2
  y0 = y - length/2
  y1 = y + length/2
  
  # draw the 3 line segments of the H-Tree
  drawLine(x0, y0, x0, y1)	
  drawLine(x1, y0, x1, y1)	
  drawLine(x0,  y, x1,  y)	
  
  newLength = length/√2
  
  drawHTree(x0, y0, newLength, depth-1)	// lower left  H-tree
  drawHTree(x0, y1, newLength, depth-1)	// upper left  H-tree
  drawHTree(x1, y0, newLength, depth-1)	// lower right H-tree
  drawHTree(x1, y1, newLength, depth-1)	// upper right H-tree
