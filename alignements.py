def ligne(liste,n,j):
    """ne fonctionne que pour aligner 5 pièces"""
    for i in range(n-j):
        for x in range(n+1):
                if liste[x][i] == liste[x][i+1] == liste[x][i+2] == liste[x][i+3] == liste[x][i+4]:
                    return True
