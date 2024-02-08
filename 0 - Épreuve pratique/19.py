ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def recherche (tab ,n):
    i=0
    if t[i]==n:
        return i
    for i in range(1,len(tab)):
        if t[i]==n:
            return i  
        
    return -1
def position_alphabet(lettre):
    return ord(lettre) - ord('A')


def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = ( position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat +=c
    return resultat
