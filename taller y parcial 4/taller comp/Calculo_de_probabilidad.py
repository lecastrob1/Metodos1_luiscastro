import numpy as np

def prob(tomadas,despues):
 N=int(1e6)
 espadas = 13-tomadas
 cartasotras = 39
 logrado = 0

 for i in range(N):
  deck = ['espada']*(espadas) + ['otro']*(cartasotras)
  np.random.shuffle(deck)
  take=deck[:despues]

  if all(elemento == 'espada' for elemento in take):
    logrado+=1
 return logrado/N
# a) Probabilidad de que las siguientes 3 cartas también sean espadas después de sacar 2 espadas
print(f"a) {prob(2, 3)}")

# b) Probabilidad de que las siguientes 2 cartas también sean espadas después de sacar 3 espadas
print(f"b) {prob(3, 2)}")

# c) Probabilidad de que la siguiente carta también sea una espada después de sacar 4 espadas
print(f"c) {prob(4, 1)}")




