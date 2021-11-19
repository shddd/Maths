import matplotlib.pyplot as plt
from math import sqrt

def afficherSegment(a, b, x, y) :
  plt.plot([a, x], [b, y], color="black")

 

def kochRec(n, a, b, x, y) :
  if not n :
    afficherSegment(a, b, x, y)
    return
  
  dx, dy = (x - a) / 3, (y - b) / 3

  kochRec(n - 1, a, b, a + dx, b + dy)
  kochRec(n - 1, a + 2 * dx, b + 2 * dy, x, y)
  
  xi, yi = a + dx + (dx / 2 - sqrt(3) * dy / 2), b + dy + (dy / 2 + sqrt(3) * dx / 2)
  kochRec(n - 1, a + dx, b + dy, xi, yi)
  kochRec(n - 1, xi, yi, a + 2 * dx, b + 2 * dy)    

def Koch(n) :
  xa, ya = 0, 0
  xb, yb = 1, 0
  xc, yc = 1 / 2, sqrt(3) / 2
  kochRec(n, xa, ya, xc, yc)
  kochRec(n, xc, yc, xb, yb)
  kochRec(n, xb, yb, xa, ya)  

def flocon(n) :
  Koch(n)
  plt.axis("off")
  plt.axis("scaled")
  plt.show()   

# Test flocon(3)
