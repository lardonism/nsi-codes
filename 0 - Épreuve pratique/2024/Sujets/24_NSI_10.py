def moyenne(notes):
    coef = 0
    note = 0
    for e in notes:
        coef = coef+e[1]
        note = note+e[0]*e[1]
    if coef == 0:
        return None
    else:
        return note/coef

coeur = [[0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
        des "*" , les 0 par un espace " " '''
    for ligne in dessin:
        affichage = ''
        for col in ligne:
            if col == 1:
                affichage = affichage + "*"
            else:
                affichage = affichage + " "
        print(affichage)


def liste_zoom(liste_depart,k):
    '''renvoie une liste contenant k fois chaque élément de
       liste_depart'''
    liste_zoomee = []
    for e in  liste_depart:
        for i in range(k):
            liste_zoomee.append(e)
    return liste_zoomee

def dessin_zoom(grille,k):
    '''renvoie une grille où les lignes sont zoomées k fois
       ET répétées k fois'''
    grille_zoomee=[]
    for ligne in grille:
        ligne_zoomee = liste_zoom(ligne,k)
        for i in range(k):
            grille_zoomee.append(ligne_zoomee)
    return grille_zoomee

