def nbr_occurrences(chaine):
    occ = {}
	   for elm in chaine:
		     if elm in occ:
			       occ[elm] +=  1
		     else: 
			       occ[elm] = 1
	   return occ


valeurs = [100, 50, 20, 10, 5, 2, 1]

def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return ... 
    v = valeurs[rang]
    if v <= ...: 
        return ... + rendu_glouton(a_rendre - v, rang) 
    else:
        return rendu_glouton(a_rendre, ...) 


