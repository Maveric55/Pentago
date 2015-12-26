"""ne fonctionne que pour aligner 5 pièces"""

def ligne(liste,n,j):
    for i in range(n-j):
        for x in range(n+1):
                if liste[x][i] == liste[x][i+1] == liste[x][i+2] == liste[x][i+3] == liste[x][i+4]:
                    return True

def colonne(liste,n,j):
   for i in range (n+1):
       for x in range (n-j):
           if liste[x][i] == liste[x+1][i] == liste[x+2][i] == liste[x+3] == liste[x+4][i]:
               return True
             
"""j'ai pas vérifié si les diagonales marchent"""
def diagonalegauche(liste,n,j):
    for i in range (n-j):
        for x in range (n-j):
            if liste[x][i] == liste[x+1][i+1] == liste[x+2][i+2] == liste[x+3][i+3] == liste[x+4][i+4]:
                return True

def diagonaledroite(liste,n,j):
    for i in range (-1,-(n-j)):
        for x in range (n-j):
            if liste[x][i] == liste[x+1][i-1] == liste[x+2][i-2] == liste[x+3][i-3] == liste[x+4][i-4]:
                return True
