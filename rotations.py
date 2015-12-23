def rotateright(liste):
    liste = [list(liste) for liste in (zip(*liste[::-1]))]

def rotateleft(liste):
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    liste = [list(liste) for liste in (zip(*liste[::-1]))]
    liste = [list(liste) for liste in (zip(*liste[::-1]))]

def rotation(liste,cadran,sens):
    if sens == True:
        if cadran == 1:
            cadran1 = liste.copy()
            for i in range(len(liste)//2):
                cadran1.pop(i-len(liste)//2)
                for x in range(len(cadran1)//2 +1):
                    cadran1[x].pop(-1)
