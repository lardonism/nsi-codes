def multiplication(n1,n2):
    n3 = 0
    for i in range(n2):
        n3 = n3 + n1
    return n3




def chercher(tab,x,i,j):
    if i > j :
        return None
    m= (i+j) // 2
    if tab[m]< x:
        return chercher(tab,x,m+1,j)
    elif tab[m]> x:
        return chercher(tab,x,m-1)
    else:
        return m

David
