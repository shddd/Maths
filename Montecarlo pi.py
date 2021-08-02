#probabilité
#Méthode de Monte-Carlo
#But : Calculer pi
#Méthode : prendre des points dans un carré 1x1cm. Le cercle x²+y² =< 1 a pour superficie pi/4. Prendre pseudo-aléatoirement des points, pour estimer la superficie.


import random

n = int(input("nbr?"))
M = 0
T = 0
for i in range(n):
  x = random.uniform(0, 1)
  y = random.uniform(0, 1)
  if ( ((x**2 + y**2) == 1) | ((x**2 + y**2) < 1) ) :
    M = M +1
    T = T+1
  else :
    T = T+1
print(M/T * 4)
