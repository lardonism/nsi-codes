def annee_temperature_minimale(temp, date):
    minit = temp[0]
    minid = date[0]
    for i in range(len(temp)):
        if temp[i] < minit:
            minit = temp[i]
            minid = date[i]
    return minit, minid





def inverse_chaine(chaine):
    '''Retourne la chaine inversée'''
    resultat = ""
    for i in range len(chaine):
        resultat += chaine[-i]
    return resultat

def est_palindrome(chaine):
    '''Renvoie un booléen indiquant si la chaine ch
    est un palindrome'''
    inverse = inverse_chaine(chaine)
    if chaine == inverse:
        return True
    return False 

def est_nbre_palindrome(nbre):
    '''Renvoie un booléen indiquant si le nombre nbre 
    est un palindrome'''
    chaine = str(nbre) 
    return est_palindrome(chaine)



