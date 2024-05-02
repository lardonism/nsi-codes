class Labyrinthe:
    """Représente un labyrinthe"""
    def __init__(self, n, m):
        """Labyrinthe, int, int -> None
        Initialise un labyrinthe vide """
        assert n%2 == 1 and m%2 == 1
        self.dim = n, m
        self.murs = [[0 for j in range(m)]
                    for i in range(n)]

    def est_dans(self, bloc):
        """ Labyrinthe, (int, int) -> bool
        Détermine si bloc est un indice de bloc valide pour le labyrinthe self """
        pass
    
    def est_sol(self, bloc):
        """ Labyrinthe, (int, int) -> bool
        Détermine si bloc est un indice de bloc valide correspondant à un sol dans le labyrinthe self """
        pass
    
    def blocs_possibles(self, position, visites):
        """ Labyrinthe, (int, int), {(int, int)} -> [(int, int)]
        Renvoie la liste des blocs voisins et non visités """
        pass
    
    def generer(self):
        """ Labyrinthe
        Génère un labyrinthe de manière aléatoire """
        pass
    
    def afficher(self):
        """ Labyrinthe -> None
        Affiche le labyrinthe self à l'écran """
        pass
