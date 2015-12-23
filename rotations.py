def rotateright(liste):
    liste = [list(liste) for liste in (zip(*liste[::-1]))]

def rotateleft(liste):
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    liste = [list(liste) for liste in (zip(*liste[::-1]))]

def rotation(liste,cadran,sens):
    """True c'est rotation vers la droite"""
    if sens == True:
        """Le 1 désigne le cadran en haut à droite"""
        if cadran == 1:
            cadran1 = liste.copy()
            for i in range(len(liste)//2):
                cadran1.pop(i-len(liste)//2)
                for x in range(len(cadran1)//2 +1):
                    cadran1[x].pop(-1)
                    """Là si tu printes une liste que t'as utilisé en exemple elle est découpée aussi"""
